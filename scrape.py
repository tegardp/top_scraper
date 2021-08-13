import html
import json
import pandas as pd
import requests
import sys
from datetime import datetime

def URLEncoding(text):
    """Converts unicode to HTML entities.  For example '&' becomes '&amp;'."""
    text = text.replace(" ", "%20")
    return text

url = "https://gql.tokopedia.com/"

searched_product = URLEncoding(sys.argv[1])
current_time = datetime.now().strftime("%Y%m%d_%H_%M_%S")
payload = [
    {
        "operationName": "SearchProductQueryV4",
        "variables": {"params": f"device=desktop&navsource=home&ob=1&page=1&q={searched_product}&related=true&rows=200&safe_search=false&scheme=https&shipping=&source=search&st=product&start=0&topads_bucket=true&unique_id=40c9c1c05db7d3c6e1807da783bdf156&user_addressId=60593885&user_cityId=176&user_districtId=2276&user_id=6362870&user_lat=-6.165523777166671&user_long=106.85870291959058&user_postCode=10640&variants="},
        "query": """query SearchProductQueryV4($params: String!) {
  ace_search_product_v4(params: $params) {
    header {
      totalData
      totalDataText
      processTime
      responseCode
      errorMessage
      additionalParams
      keywordProcess
      __typename
    }
    data {
      products {
        id
        name
        ads {
          adsId: id
          productClickUrl
          productWishlistUrl
          productViewUrl
          __typename
        }
        badges {
          title
          imageUrl
          show
          __typename
        }
        category: departmentId
        categoryBreadcrumb
        categoryId
        categoryName
        countReview
        discountPercentage
        gaKey
        imageUrl
        labelGroups {
          position
          title
          type
          url
          __typename
        }
        originalPrice
        price
        priceRange
        rating
        ratingAverage
        shop {
          id
          name
          url
          city
          isOfficial
          isPowerBadge
          __typename
        }
        url
        wishlist
        sourceEngine: source_engine
        __typename
      }
      __typename
    }
    __typename
  }
}
"""
    }
]
headers = {
    "cookie": "_gcl_au=1.1.1893142307.1623466018; _SID_Tokopedia_=JhQS6Mly6bp5-4XqQ6EmhOI3Weu17muIed9_Qu5TE4jo83XXUTCpLle9rKW9PA1ikVpwb4-cCrhbsQ2dFj4sJlSiiCFl8RplqKCWKR2dPDF_kreoSyGNXMKBfIaQo0VZ; DID=5c5ba2519a7e6e66876f81ec344648d4d7ddc8675ec88c411edcc46a5e7fb0a340651c5a350dbfb04fe70ff2832c26c2; DID_JS=NWM1YmEyNTE5YTdlNmU2Njg3NmY4MWVjMzQ0NjQ4ZDRkN2RkYzg2NzVlYzg4YzQxMWVkY2M0NmE1ZTdmYjBhMzQwNjUxYzVhMzUwZGJmYjA0ZmU3MGZmMjgzMmMyNmMy47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=; _UUID_NONLOGIN_=1ba614b2b64027f7c99c8912958e1217; __auc=082ca7a7179fe1da13e0fb2f12e; l=1; TOPATK=m8ljTG5ZQBiXfm9GlsIf5A; _hjid=1b0fbb0b-48e6-412e-858e-99e30e867e90; S_L_c637addebe6afd84bf57eb18b11b0f80=7a45025e8b52477a2de873f197f431a8~20210910094737; TOPRTK=kfPUc-vhSayVuMZQZlJF2Q; aus=1; _jx=e927eb90-cb28-11eb-836d-2fa066da6444; _gcl_aw=GCL.1626737251.Cj0KCQjwxdSHBhCdARIsAG6zhlV3iglmNv73UVDJMSFBRHcIDDqqHBfgJeB4i46RoYNMwwZfgATsJ94aAu70EALw_wcB; _gcl_dc=GCL.1626737251.Cj0KCQjwxdSHBhCdARIsAG6zhlV3iglmNv73UVDJMSFBRHcIDDqqHBfgJeB4i46RoYNMwwZfgATsJ94aAu70EALw_wcB; _gac_UA-126956641-6=1.1626737253.Cj0KCQjwxdSHBhCdARIsAG6zhlV3iglmNv73UVDJMSFBRHcIDDqqHBfgJeB4i46RoYNMwwZfgATsJ94aAu70EALw_wcB; _gac_UA-9801603-1=1.1626737322.Cj0KCQjwxdSHBhCdARIsAG6zhlV3iglmNv73UVDJMSFBRHcIDDqqHBfgJeB4i46RoYNMwwZfgATsJ94aAu70EALw_wcB; _CAS_=%7B%22dId%22%3A2276%2C%22aId%22%3A60593885%2C%22lbl%22%3A%22Kontrakan%20Kemayoran%20Tegar%20Dani%20Pratama%22%2C%22cId%22%3A176%2C%22long%22%3A%22106.85870291959058%22%2C%22lat%22%3A%22-6.165523777166671%22%2C%22pCo%22%3A%2210640%22%2C%22wId%22%3A0%2C%22sId%22%3A11530573%7D; _gid=GA1.2.1497166530.1628532420; tuid=6362870; zarget_visitor_info=%7B%7D; zarget_user_id=82e6f630-20c0-4e6a-f2d4-314137bb8637; bm_sz=3E756341B7A8B6084B948A0134427AEA~YAAQTNrIFzt2VdV6AQAAGCUmPgwBsWFAE+IjiyJWc8OxMGsI8Ee7uS/usJRizCjlRdwjD1iZcXOjOFxOO7OKadsGn+8Ag9pYZFA8Ez7zWnFk9UIxi37waNiqFNNHArf2CORiY7W6EE6ftKJDjbtBk7fTwG7JsOT9tGcVaLdixAVWm0uDoickJNWwEvgrYcUzSl/H3wbh3HRHI828fm+NUmdtu+W9CfusBqwZSye9Q//u7x2+KVv26HmaKk7ycZIXaK6KgxoJZcHKIKY53OLDO54o6K9sCy+MfHrDC4rh9VFs/1e8XccU4ot1id7jIULMzOQt6NqckNK1/k0GxQs=~3491122~3163702; ak_bmsc=1396F4F83EC2390A5BDCD5739A88C4CA~000000000000000000000000000000~YAAQTNrIF/V2VdV6AQAAoFYmPgyB85tjcPVUmzn2qJrjNdUjVGMOhaE68VQJz5ckNA/HXt/sYb4E+GLyAR1a6GtBc1uEVg4yCCUJL60WEFoYLTtWGuNz28msOiqnIw4RM8JRPKIfucRlZf4Xy4VOWBbY9IQ4OwEr771wPL21mVNl8zh7WGJxJ95Ws+ABPQd2sj4gq2QhKWe0ehxL1VaC6VMpi2M+Ibl4z56ZU5KOWdRM62Mj46n/ZSFU3UZ8rDlTQYGfpo5PvKAGR1fnMZ16euwRJImMtdfswhKu/rWos5/6zudwfBploRoXlLSAz1Z/kLDbICdPkC7M3R1+DDavNpF8tEZj50ocYaypLddw3avsayLztcouPyNLXE0CTn0vqu4q92s/KTIZETFJDY/E; __asc=34b250c917b3e266aac864d6dd0; _jxs=1628835316-e927eb90-cb28-11eb-836d-2fa066da6444; bm_mi=CDFC7233E8C901ADABB4F91F0D42245F~eaQrnsjn+xzoJ+CMjMwoWiQyLAyYN+ZBsSg4uWW7p4F2WtFgZvUd46qLlgZa3R2H6FD9iA2fa3+mCxP0WNA6KOg1C86Frf/Q9fnG7Q/R5XXKrhHQPT1NmXJNecfZZyjo425IFSImmjKUUD/BwRZttlsgnKMio61SHADzOc8sUomaoU85rr81yzhI9lhV3kwwC3C6J5RepaWr79QGZ/zPrL3ITtK0XwigESy0f1Y4CYY=; bm_sv=46AAEC7C8D47087DB8EF309C7A635F68~TmogZBc7+jYCP7VTY3qNODF2m/ecTX23jSckquZ89hD8cYyAcXAF/ItTYGt7uSCcAz3FwCyS6t62dAXKKBHalgIJtqm3TO3qvfsSJtH4hArM0JNAS5rtOZAOK+9NLNUxb/n4+tvdbq7T0QG03fERfdxI23XMxCJrexc4Q76egeo=; cto_bundle=fQhCCl9qZkh0cHRZVE9nQzZaUmU5QVBDTG90b0N1aTRDUmZlUWVaTkV4Q2lyc3Bmb0VBSzRsRGNJQTRBNCUyQmFBejRPSjBBdXdyN1dxZ2dkRHFxaUFFb3Z1TW92Ukx5czFRM1dtWVVXQm54WXY5YVN1RXJHc01DQUZGejElMkZ3aXJiM3lrUXJMQmRub1NtMGI2eTZqVWM1SG4xckN3JTNEJTNE; _gat_UA-9801603-1=1; _dc_gtm_UA-9801603-1=1; _dc_gtm_UA-126956641-6=1; _ga_70947XW48P=GS1.1.1628835305.78.1.1628839308.53; _ga=GA1.2.457170352.1623466019; _abck=6DF1286EAF99A199A8B707883B25516C~0~YAAQvu84F0qcCq96AQAAentjPgYlnq85GjebevTlweGxjTfSkqam5JCMaGs+nxyu24rWt3vMYAS3ra6sPSJpzyEcDTMliPjl0goOStAgVDMZbPlSjM99tRvQlOZg+srxFc13CoMTcRwSgm3sjfNfSR5U/rAY6FO1dW++JCLj+iDcuOr1ME9kqtR0GvnUs4UViBsdbbxv3u+ykqittXkA7WLTdcBJ8qeJxJlctb5frf9sLc8LG5nPfZwQJ3fzap+lCukkxbOYtZq5FcKoj9F9GmwtP05su57fWa+X94Lieq1AlmxVJElKfXHCjcC4B32yihZVXMrSDxtTtNWCQ6wJeDFgq80fEgMObG9BktCpHrPmSjF94+hr3gepEtgl33pM1ic=~-1~-1~-1",
    "authority": "gql.tokopedia.com",
    "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"',
    "tkpd-userid": "6362870",
    "sec-ch-ua-mobile": "?0",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67",
    "content-type": "application/json",
    "accept": "*/*",
    "x-version": "fa84ae1",
    "x-source": "tokopedia-lite",
    "x-device": "desktop-0.0",
    "x-tkpd-lite-service": "zeus",
    "origin": "https://www.tokopedia.com",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.tokopedia.com/search?st=product&q=xiaomi&navsource=home",
    "accept-language": "en-US,en;q=0.9,id;q=0.8"
}

response = requests.request("POST", url, json=payload, headers=headers)

jsondata = json.loads(response.text)

df = pd.DataFrame.from_records(jsondata[0]["data"]["ace_search_product_v4"]["data"]["products"])

df.to_csv(f"{searched_product}_{current_time}.csv")