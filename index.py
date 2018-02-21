#!/usr/bin/env python

print "Content-type: text/html\n\n"
print

print "<html>"
print "<head>"
print '<meta charset="UTF-8">'
print '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
print '<meta http-equiv="X-UA-Compatible" content="ie=edge">'
print "<title>Alarm ticket</title>"
#<!-- css -->
print '<link rel="stylesheet" href="/css/app.css">'
#<!-- Bootstrap 3.3.7 -->
print '<link rel="stylesheet" href="/cgi-enabled/AdminLTE-2.4.2/bower_components/bootstrap/dist/css/bootstrap.min.css">'
#<!-- DataTables -->
print '<link rel="stylesheet" href="/cgi-enabled/AdminLTE-2.4.2/bower_components/datatables.net-bs/css/dataTables.bootstrap.min.css">'
#<!-- Font Awesome -->
print '<link rel="stylesheet" href="/cgi-enabled/AdminLTE-2.4.2/bower_components/font-awesome/css/font-awesome.min.css">'
#<!-- Ionicons -->
print '<link rel="stylesheet" href="/cgi-enabled/AdminLTE-2.4.2/bower_components/Ionicons/css/ionicons.min.css">'
#<!-- jvectormap -->
print '<link rel="stylesheet" href="/cgi-enabled/AdminLTE-2.4.2/bower_components/jvectormap/jquery-jvectormap.css">'
#<!-- Theme style -->
print '<link rel="stylesheet" href="/cgi-enabled/AdminLTE-2.4.2/dist/css/AdminLTE.min.css">'
#<!-- AdminLTE Skins. Choose a skin from the css/skins
#    folder instead of downloading all of them to reduce the load. -->
print '<link rel="stylesheet" href="/cgi-enabled/AdminLTE-2.4.2/dist/css/skins/_all-skins.min.css">'

#<!-- css in alarm ticket content -->
print '<link rel="stylesheet" href="/css/alarm_ticket.css">'

print "</head>"
print "<body>"

# from MySQL import Database
# db = Database(host='127.0.0.1', username='root', password='', db='alarm_ticket')
# select_catid = """ SELECT `cat_id`,`host` FROM `splunk` WHERE '1'"""
# lst_catid = db.query(select_catid)
# print lst_catid

print '<nav class="navbar-default">'
print '<div class="container-fluid">'
print '<div class="navbar-header">'
print '<a class="navbar-brand" href="/cgi-enabled/index.py">Alarm Ticket</a>'
print "</div>"
print '<ul class="nav navbar-nav">'
# print '<li class="active"><a href="/home">Home</a></li>'
# print '<li><a href="/splunk">Splunk</a></li>'
print "</ul>"
print "</div>"
print "</nav>"

print '<div class="box">'
print '<div class="box-body ">'
print '<div class="table-responsive">'
print '<table class="table table-bordered table-striped" id="alarmtickets">'
print "<thead>"
print '<tr class="Bg-head-table">'
print '<th class="col-lg-1">Ticket No.</th>'
print '<th class="col-lg-1">Cat ID</th>'
print '<th class="col-lg-1">Source Interface</th>'
print '<th class="col-lg-1">Host</th>'
print '<th class="col-lg-1">Hostname</th>'
print '<th class="col-lg-1">device_time</th>'
print '<th class="col-lg-1">Port Status</th>'
print '<th class="col-lg-1">Path</th>'
print '<th class="col-lg-1">flap</th>'
print '<th class="col-lg-1">Ticket Status</th>'
print '<th class="col-lg-1">Affected Service</th>'
print '<th class="col-lg-1"></th>'
print "</tr>"
print "</thead>"
print "<tbody>"


print "</tbody>"
print "</table>"
print "</div>"
print "</div>"
print "</div>"

print '<script src="/cgi-enabled/js/app.js"></script>'
print '<script src="/cgi-enabled/js/main.js"></script>'
#@if(request()->path() == 'tts')
print '<script src="/cgi-enabled/js/tts.js"></script>'
#@endif
#<!-- jQuery 3 -->
print '<script src="/cgi-enabled/AdminLTE-2.4.2/bower_components/jquery/dist/jquery.min.js"></script>'
print '<script src="/cgi-enabled/js/jquery-3.3.1.min.js"></script>'
#<!-- Bootstrap 3.3.7 -->
print '<script src="/cgi-enabled/AdminLTE-2.4.2/bower_components/bootstrap/dist/js/bootstrap.min.js"></script>'
#<!-- DataTables -->
print '<script src="/cgi-enabled/AdminLTE-2.4.2/bower_components/datatables.net/js/jquery.dataTables.min.js"></script>'
print '<script src="/cgi-enabled/AdminLTE-2.4.2/bower_components/datatables.net-bs/js/dataTables.bootstrap.min.js"></script>'
#<!-- FastClick -->
print '<script src="/cgi-enabled/AdminLTE-2.4.2/bower_components/fastclick/lib/fastclick.js"></script>'
#<!-- AdminLTE App -->
print '<script src="/cgi-enabled/AdminLTE-2.4.2/dist/js/adminlte.min.js"></script>'
#<!-- Sparkline -->
print '<script src="/cgi-enabled/AdminLTE-2.4.2/bower_components/jquery-sparkline/dist/jquery.sparkline.min.js"></script>'
#<!-- SlimScroll -->
print '<script src="/cgi-enabled/AdminLTE-2.4.2/bower_components/jquery-slimscroll/jquery.slimscroll.min.js"></script>'
print "</body>"
print "</html>"
