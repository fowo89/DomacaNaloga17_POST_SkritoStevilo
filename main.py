#!/usr/bin/env python
import os
import jinja2
import webapp2
import random

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")

class CalculateHandler(BaseHandler):
    def post(self):
        skrito_stevilo = random.randint(1,5)

        if int(self.request.get("poskus1")) != skrito_stevilo and int(self.request.get("poskus1")) <= 5 and int(self.request.get("poskus1")) >= 1:
            rezultat = "Skrito stevilo ni " + self.request.get("poskus1") + "! Poskusite znova!"


        elif int(self.request.get("poskus1")) == skrito_stevilo:
            rezultat = "Bravo! Uganili ste!"

        else:
            rezultat = "Prosim vnesite stevilo med 1 in 5!"



        podatki={"rezultat": rezultat}
        return self.render_template("rezultat.html", podatki)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/rezultat', CalculateHandler),
], debug=True)
