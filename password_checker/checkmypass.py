#check if the password has ever been hacked
#It will help you pick a password that has never been found
import requests
import hashlib
import sys

#Function for the API to query
def request_api_data(query_char):
#CFBDA is the first 5 symbols of a hash of password123
      url = "https://api.pwnedpasswords.com/range/" + query_char
      res = requests.get(url)
      if res.status_code != 200:
            raise RuntimeError(f"Error fetching: {res.status_code}, check the API and try again!") 
      return res #res is response

#need to be able to read the response
#we want to know the # of times this password has been leaked in the past
def get_password_leaks_count(hashes, hash_to_check):
      hashes = (line.split(":") for line in hashes.text.splitlines())
      for h, count in hashes:
            if h == hash_to_check:
                  return count
      return 0

#check if password exists in the API
def pwned_api_check(password):
      #hash password, in uppercase like pwned website
      sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
      #we only need the first 5 characters of password to send to API
      first5_char, tail = sha1password[:5], sha1password[5:]
      response = request_api_data(first5_char)
      return get_password_leaks_count(response, tail)
      
def main(args):
      for password in args:
            count = pwned_api_check(password)
            if count:
               print(f"{password} was found {count} times. You should change your password!")
            else:
                  print(f"{password} was NOT found. Carry on!")
      return "Done!"
      
#make sure it is being run as a main file and not as an import
if __name__ == "__main__":
      #make sure you exit the file
      sys.exit(main(sys.argv[1:]))