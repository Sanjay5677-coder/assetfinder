from flask import Flask, render_template, request, jsonify
import requests
import json
import socket
from bs4 import BeautifulSoup
import dns.resolver


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form['url']
    respon = requests.get(url)
    soup = BeautifulSoup(respon.text, 'html.parser')

    # Extract the desired data from the soup object
    # Modify this part according to your specific scraping requirements
    #domain = 'archive.org'  # Replace with the domain for which you want to retrieve DNS servers
    data=soup.find_all(text=True)
    # Perform DNS lookup to fetch the DNS servers
    #domain = request.form.get('url')
    #domain='dnsdumpster.com'  working well 
    
    # im=[]
    # try:
         

    #      _, _, ips = socket.gethostbyname_ex(url)
    #      dns_servers = ips
    # except socket.gaierror:
    #      dns_servers = []
        
    # im.append(dns_servers) 
   
        
    # url = request.form.get('url')    
    # dns_servers = socket.gethostbyname_ex(soup)[2]
    # respons = {'domain': soup, 'dns_servers': dns_servers}
     
    response = requests.get(url)
    raw_text = response.text.strip()

    # Create a dictionary to hold the scraped data
    data1 = {
        'scraped_data': raw_text
    }
    
    response = requests.get(url)
    if response.status_code == 200:
        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Perform the web scraping to extract all the data
        scraped_data = []
        for element in soup.find_all():
            data2 = {'tag': element.name, 'text': element.get_text(strip=True)}
            scraped_data.append(data2)

        # Return the scraped data in JSON format
        #return jsonify(scraped_data)
    #else:
        #return 'Failed to scrape the website.'


    # Return the data as JSON
    # url = request.form.get('url')

    # if not url:
    #     return jsonify({'error': 'Please provide a URL in the request body.'}), 400

    # try:
    #     dns_servers = dns.resolver.query(url, 'NS')
    #     dns_list = [str(server) for server in dns_servers]
    #     return jsonify({'url': url, 'DNS Search': dns_list})
    # except dns.resolver.NXDOMAIN:
    #     return jsonify({'error': 'Invalid domain name.'}), 400
    # except dns.resolver.NoAnswer:
    #     return jsonify({'error': 'No DNS servers found for the given domain.'}), 400
    # except Exception as e:
    #     return jsonify({'error': str(e)}), 500    
    
    # # Return the DNS servers as JSON
    return jsonify( {f'Host Search:<{url}><{dns_servers}> Result ':data},{f'Text Search:<{url}> Result':data1},{f'4.Host Search:<{url}>':scraped_data})
    #data=soup.find_all(text=True)
    # Example: Extract all paragraph tags
    
    #return jsonify(data)

    # Return the data in JSON format
    

if __name__ == '__main__':
    app.run(debug=True)
