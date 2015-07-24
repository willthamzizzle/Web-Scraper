#!/bin/env ruby


require 'rubygems'
require 'nokogirl'
require 'open-uri'


page Nokogiri::HTML(
open("http://rcm.corp.emc.com/Systems/RCM_Schedule/schedule.php"))

# Nokogiri::HTML::Document
puts page.class
