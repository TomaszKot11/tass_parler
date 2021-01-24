require 'csv' 

CSV_FILE_NAME = 'following_pairs_200_0.csv'

# około 3000 par profile, following_profile
csv_file_opened = CSV.read(File.read(CSV_FILE_NAME), headers: false)


# https://dev.to/jolouie7/ruby-each-map-reduce-unless-and-until-3b5c
csv_file_opened.each do |el|
    puts "Witam #{el}"
end

