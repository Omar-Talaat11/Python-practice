import webbrowser

facebook_link = 'https://www.facebook.com/'

linkedin_link = 'https://www.linkedin.com/'

github_link = 'https://github.com/Omar-Talaat11'

def firefox(url):
    webbrowser.get('firefox').open(url)
    
def available_links():
    return {'facebook_link':facebook_link,'linkedin_link':linkedin_link,'github_link':github_link}