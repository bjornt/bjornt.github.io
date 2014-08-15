---
layout: post
title: Using web.go on Google App Engine
date: 2011-11-07 13:50:46
tags:
 - golang
 - google-app-engine
---

In short, if you want to use [`web.go`](http://www.getwebgo.com/) in
[Google App Engine's Go runtime environment](http://code.google.com/appengine/docs/go/overview.html), check out
[my `google-app-engine` branch of `web.go`](https://github.com/bjornt/web.go/tree/google-app-engine).
Using that one you can start using `web.go` like this:

    package webgoexample

    import (
        "http"
        "log"
        "os"
        "web"
    )

    var server *web.Server

    func init() {
        server = &web.Server{
            Config: web.Config,
            Logger: log.New(os.Stdout, "", log.Ldate|log.Ltime)}
        server.Get("/", func(ctx *web.Context) {
            ctx.Write([]uint8("Hello from web.go!"))
        })

        // Send all requests to web.go.
        http.HandleFunc("/", handler)
    }

    func handler(writer http.ResponseWriter, request *http.Request) {
        server.ServeHTTP(writer, request)
    }

BTW, if you simply put the [`web.go`](http://www.getwebgo.com/) branch in your root dir,
you have to remove the `examples/` directory, otherwise [App Engine](http://code.google.com/appengine/) won't be able to compile your
project.

The branch in question has quite minimal changes to `web.go`, but I haven't
proposed to merge it to trunk yet, since it removes some functionality. First
of all I changed it not to set up `/debug/` paths, so that I could remove the
use of `http/pprof`, since it's not available on [App Engine](http://code.google.com/appengine/). After that I had
to also remove the use of `net.ResolveTCPAddr`, which is also not available on
App Engine. I basically replaced it with `net.SplitHostPort`, which I suspect
is good enough. It doesn't resolve host names and port names, but I'd be
surprised if `hr.RemoteAddr` wouldn't be an IP address and a port number.
