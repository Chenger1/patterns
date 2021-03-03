from abc import ABC, abstractmethod, abstractproperty


class Site:
    def __init__(self):
        self._parts = []

    def add(self, part):
        self._parts.append(part)

    def __str__(self):
        return 'Site: ' + ', '.join(self._parts)

class Documentation:
    def __init__(self):
        self._parts = {}

    def add(self, key, value):
        self._parts.update({key: value})

    def __str__(self):
        return 'Docs: ' + ', '.join(self._parts)


class Builder(ABC):
    def __init__(self):
        self.reset()

    @abstractmethod
    def reset(self):
        self._product = None

    @abstractmethod
    def setFrontPage(self, UI):
        pass

    @abstractmethod
    def setAdminPage(self):
        pass

    @abstractmethod
    def setPremiumFeature(self, package):
        pass

    def getProduct(self):
        product = self._product
        self.reset()
        return product


class SiteBuilder(Builder):
    def reset(self):
        self._product = Site()

    def setFrontPage(self, UI):
        self._product.add(UI)

    def setAdminPage(self):
        self._product.add('AdminPage')

    def setPremiumFeature(self, package):
        self._product.add(f'Set of features: {package}')


class SiteDocumentationBuilder(Builder):
    def reset(self):
        self._product = Documentation()
    
    def setFrontPage(self, UI):
        self._product.add("UI-docs", UI)

    def setAdminPage(self):
        self._product.add('AdminPage-docs', 'adminpage')

    def setPremiumFeature(self, package):
        self._product.add('Advanced feature', package)


class Director:
    def __init__(self):
        self._site_builder = None
        self._documentation_builder = None

    @property
    def site_builder(self):
        return self._site_builder

    @site_builder.setter
    def site_builder(self, build):
        self._site_builder = build

    @property
    def documentation_builder(self):
        return self._documentation_builder

    @documentation_builder.setter
    def documentation_builder(self, build):
        self._documentation_builder = build

    def build_minimal_product(self, UI):
        self._site_builder.setFrontPage(UI)
        self._site_builder.setAdminPage()

        self._documentation_builder.setFrontPage(UI)
        self._documentation_builder.setAdminPage()

        return self._site_builder.getProduct(), self._documentation_builder.getProduct()

    def build_premium_product(self, UI, package):
        self._site_builder.setFrontPage(UI)
        self._site_builder.setAdminPage()
        self._site_builder.setPremiumFeature(package)

        self._documentation_builder.setFrontPage(UI)
        self._documentation_builder.setAdminPage()
        self._documentation_builder.setPremiumFeature(package)
        return self._site_builder.getProduct(), self._documentation_builder.getProduct()


if __name__ == '__main__':
    director = Director()
    site_builder = SiteBuilder()
    documentation_builder = SiteDocumentationBuilder()
    director.site_builder = site_builder 
    director.documentation_builder = documentation_builder

    site, docs = director.build_minimal_product('UI')
    print(site)
    print(docs)
    print('\n')

    site, docs = director.build_premium_product('UI', 'Premuim Package')
    print(site)
    print(docs)
    print('\n')

    site_builder.setFrontPage('Custom UI')
    site_builder.setPremiumFeature('Custom Feature')
    site = site_builder.getProduct()
    print(site)