from abc import ABC, abstractmethod


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
    def set_front_page(self, UI):
        pass

    @abstractmethod
    def set_admin_page(self):
        pass

    @abstractmethod
    def set_premium_feature(self, package):
        pass

    def get_product(self):
        product = self._product
        self.reset()
        return product


class SiteBuilder(Builder):
    def reset(self):
        self._product = Site()

    def set_front_page(self, UI):
        self._product.add(UI)

    def set_admin_page(self):
        self._product.add('AdminPage')

    def set_premium_feature(self, package):
        self._product.add(f'Set of features: {package}')


class SiteDocumentationBuilder(Builder):
    def reset(self):
        self._product = Documentation()
    
    def set_front_page(self, UI):
        self._product.add("UI-docs", UI)

    def set_admin_page(self):
        self._product.add('AdminPage-docs', 'adminpage')

    def set_premium_feature(self, package):
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
        self._site_builder.set_front_page(UI)
        self._site_builder.set_admin_page()

        self._documentation_builder.set_front_page(UI)
        self._documentation_builder.set_admin_page()

        return self._site_builder.get_product(), self._documentation_builder.get_product()

    def build_premium_product(self, UI, package):
        self._site_builder.set_front_page(UI)
        self._site_builder.set_admin_page()
        self._site_builder.set_premium_feature(package)

        self._documentation_builder.set_front_page(UI)
        self._documentation_builder.set_admin_page()
        self._documentation_builder.set_premium_feature(package)
        return self._site_builder.get_product(), self._documentation_builder.get_product()


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

    site_builder.set_front_page('Custom UI')
    site_builder.set_premium_feature('Custom Feature')
    site = site_builder.get_product()
    print(site)