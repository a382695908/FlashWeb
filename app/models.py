from subprocess import Popen,PIPE

def perform_whois_query(query_string):
  """
  Perform whois query by forking jwhois. 
  Return a list of lines of query results.
  """
  p = Popen(["/usr/bin/jwhois", query_string], stdout=PIPE, stderr=PIPE)
  out, err = p.communicate()
  status = p.returncode

  print("return code: %d" % status)

  if status == 0:
    jwhois_output = out.split('\n')    
  else:
    #template expects list to iterate over to print output
    jwhois_output = ["Error, unable to complete request."]
    print("STUB: logging useful internal message here")

  return jwhois_output
