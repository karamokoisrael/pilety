from django.views.generic import  TemplateView

class Homepage(TemplateView):
    template_name = 'homepage.html'


class AboutPage(TemplateView):
    template_name = 'pilety/about.html'


class ContactPage(TemplateView):
    template_name = 'pilety/contact.html'



class PolicyPage(TemplateView):
    template_name = 'pilety/privacy-policy.html'


class ServicesPage(TemplateView):
    template_name = 'pilety/request-quote.html'


class TeamPage(TemplateView):
    template_name = 'pilety/team.html'


class TermsPage(TemplateView):
    template_name = 'pilety/terms-conditions.html'


class WhyUsPage(TemplateView):
    template_name = 'pilety/why-us-choose.html'


class PriceLiftPage(TemplateView):
    template_name = 'pilety/price_list.html'

