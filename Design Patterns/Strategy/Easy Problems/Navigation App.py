"""
Problem Statement:
------------------

Without using if-else or switch-case conditionals, 
implement multiple different navigation routes for a Navigation app.

1. Car route
2. Bike route
3. Walking route

Method to be used: build_route(source, destination)
"""


from abc import ABC, abstractmethod

class NavigationStrategy(ABC):

    @abstractmethod
    def build_route(src: str, dest: str):
        pass


class CarRouteNavigationStrategy(NavigationStrategy):

    def build_route(self, src: str, dest: str):
        print(f"Building car route from {src} to {dest}")


class BikeRouteNavigationStrategy(NavigationStrategy):

    def build_route(self, src: str, dest: str):
        print(f"Building bike route from {src} to {dest}")


class WalkingRouteNavigationStrategy(NavigationStrategy):

    def build_route(self, src: str, dest: str):
        print(f"Building walking route from {src} to {dest}")


class NavigationContext:

    def __init__(self, strategy: NavigationStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: NavigationStrategy):
        self.strategy = strategy

    def build_route(self, src: str, dest: str):
        self.strategy.build_route(src, dest)



if __name__ == "__main__":

    context = NavigationContext(CarRouteNavigationStrategy())
    context.build_route(src = "Hyderabad", dest = "Bangalore")

    context.set_strategy(BikeRouteNavigationStrategy())
    context.build_route("Gachibowli", "Maula Ali")

    context.set_strategy(WalkingRouteNavigationStrategy())
    context.build_route("DLF", "Raidurg")