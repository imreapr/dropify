from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
from webapp.utils import ProductCrawler, ProductInfo
from .forms import ProductForm

class HomeView(TemplateView):
    template_name = 'webapp/home.html'
    #in case of a get request return view
    def get(self, request):
        form = ProductForm()
        return render(request, self.template_name ,{'form' : form})
    #in case of a post request return view
    def post(self, request):

        form = ProductForm(request.POST)
        #gets user submitted text, cleans, and stores it
        if form.is_valid():
            text = form.cleaned_data['post']
            #generated link based on product_keyword
            product_search_link = "https://www.aliexpress.com/af/" + text + ".html?site=glo&g=y&origin=n&blanktest=0&filterCat=100003127%2C200003482%2C200000890&jump=afs&groupsort=1&SearchText=" + text + "&SortType=total_tranpro_desc&initiative_id=SB_20196501082864"
            #creates a crawler object for users keyword
            crawler = ProductCrawler(product_search_link)
            #crawls for information
            crawler.crawler()
            #gathers necessary data for finding product
            name = crawler.get_product_from_link(product_search_link)[0]
            price = crawler.get_product_from_link(product_search_link)[1]
            orders = crawler.get_product_from_link(product_search_link)[2]
            link = crawler.get_product_from_link(product_search_link)[3]

        args = {'form' : form, 'text' : text, 'name' : name, 'price' : price, 'orders' : orders, 'link' : link}
        return render(request, 'webapp/product.html', args)
