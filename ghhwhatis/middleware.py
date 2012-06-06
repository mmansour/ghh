#class RootSlugMiddleware(object):
#    def process_request(self, request):
#        path_parts = request.path_info.split("/")
#        if '-' in path_parts[1]:
#            print "Printing request path info from middleware: {0}".format(path_parts[1])
#        else:
#            print "- is not in there man"
#