#
# Config Class for the requirements for rmtoo
#

class Config:
    # development - team at flonatel
    # users - users from the Internet (sourceforge replies and wishes)
    # customers - people and companies who are flonatel's customers
    stakeholders = ["development", "management", "users", "customers"]
    inventors = ["flonatel", ]

    output_specs = \
        { 
          "html": ["doc/html/reqs",
                   ["doc/topics", "ReqsDocument"],
                   "doc/html/header.html",
                   "doc/html/footer.html"],
        }