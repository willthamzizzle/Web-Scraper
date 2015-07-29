#!/bin/env ruby

# Author: William Thammavong
# Date: 7/29/1015


require 'open-uri'
require 'nokogiri'

BASE_RCM_URL = "http://rcm.corp.emc.com"
LIST_URL = "#{BASE_RCM_URL}//Systems/RCM_Schedule/schedule.php"

page = Nokogiri::HTML(open(LIST_URL))


page.xpath('//h3/a').each do |node|
  puts node.text
end
