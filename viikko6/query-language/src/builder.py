from matchers import And, HasAtLeast, PlaysIn, Not, Or, HasFewerThan


class Query:
    def __init__(self, matchers = [], matcher = None):
       self.matchers = matchers[:]
       if(matcher != None):
           self.matchers.append(matcher)
    

class QueryBuilder:
    def __init__(self, query = Query()):
        self.query = query

    def plays_in(self, team: str):
        return QueryBuilder(Query(self.query.matchers, PlaysIn(team)))
    
    def has_fewer_than(self, value: int, attr: str):
        return QueryBuilder(Query(self.query.matchers, HasFewerThan(value, attr)))
    
    def has_at_least(self, value: int, attr: str):
        return QueryBuilder(Query(self.query.matchers, HasAtLeast(value, attr)))
    
    def one_of(self, *matchers):
        return QueryBuilder(Query(self.query.matchers, Or(*matchers)))
    
    def build(self):
        return And(*self.query.matchers)
    
    
    