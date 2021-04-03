from django.core.paginator import EmptyPage, Paginator


#При запросе несуществующей страницы возвращает последнюю возможную
class SafePaginator(Paginator):
    def validate_number(self, number):
        try:
            return super(SafePaginator, self).validate_number(number)
        except EmptyPage:
            if number > 1:
                return self.num_pages
            else:
                raise
