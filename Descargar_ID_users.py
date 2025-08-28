import requests
import json
import pandas as pd

with open('./Archivo_fetch.txt', 'r') as file:
    fetch_data = file.read()

urls = []
fetch_data = fetch_data.splitlines()
for line in fetch_data:
    if line.find('fetch("') != -1 and line.find("{'") == -1:
        urls.append(line.replace('fetch("',"").replace('", {', ''))

print(urls[1])

headers=   {
    "accept": "*/*",
    "accept-language": "es-US,es;q=0.9,en-US;q=0.8,en;q=0.7",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin"
}

cookies= {
  "living_user_id":"307185092517",
  " _ttp":"2w4ZgmmFQqvwMyYTGiWFLi7oej5",
  " s_v_web_id":"verify_mag41yoa_7HAdNuMV_Pi3i_4vso_Bq1o_2gGTaJWhRo1Y",

  " uid_tt":"6a2ae2f120ce2f5189447c3d0c76a2a61f6c4c625a8f5c303aae39b960eee45f",
  " uid_tt_ss":"6a2ae2f120ce2f5189447c3d0c76a2a61f6c4c625a8f5c303aae39b960eee45f",
  " sid_tt":"e891cfde4aed092e28d5166dae485b90",
  " sessionid":"e891cfde4aed092e28d5166dae485b90",
  " sessionid_ss":"e891cfde4aed092e28d5166dae485b90",
  " store-idc":"maliva",
  " store-country-code":"co",
  " store-country-code-src":"uid",
  " tt-target-idc":"useast1a",
  " tt-target-idc-sign":"pJ5Nd7mJ_V6ZIrj0WtR2NCUauOoaot8AIzMUCZhCGFn2dgXXpwcNBlZ5PnGbPxcQIaHlqjs5j4rhB_K6TY5VMfJjH_zui2nhpHR7vGN2V7zHpRpx607TQ99h4cQqALWd7u2XJOHwXPZs1_u4xRaQGOIdUwKbRExMUnD67vn8Up_m-R2T0Q7cEbtLZ9rv0N9lc0-DnMGxUY0QFDPC7zepaamueEgvl0N93Qlt2jiAqbdhA2frU8FosePpUFibvybFKwxduhntgcFCyukOR7dD7XAZ4GLWZR9EF6wKHdxZLW8V7ByyBDmIgrNqGnUsZw46-zFcyZ5WolSD64lSDIp_SLnnbaRXYTlcJhABj_7oIdLIl8CViEUhNkg5wBsuFfnrF-7nLhF8gFbLCREYaneERa1XeKQXl8EbdFfnM2Pi6mb30QB5QgawkOfpVAHyecJetRgXiSTz6HiGZFUNqrtrISoHMNeA2p_TAw_H2nqN3BqU7zgtV-GjctYPNt1wMkK4",
  " last_login_method":"facebook",
  " sid_guard":"e891cfde4aed092e28d5166dae485b90^%^7C1749774718^%^7C15551996^%^7CWed^%^2C+10-Dec-2025+00^%^3A31^%^3A54+GMT",
  " sid_ucp_v1":"1.0.0-KDg1NmQyODViY2MzYjYzNDU2OThkN2RiNzJmZDhhMzNlMWQ4Y2I4ZmMKGQiGiN6Yndi1imMQ_uKtwgYYsws4CEAKSAQQAxoGbWFsaXZhIiBlODkxY2ZkZTRhZWQwOTJlMjhkNTE2NmRhZTQ4NWI5MA",
  " ssid_ucp_v1":"1.0.0-KDg1NmQyODViY2MzYjYzNDU2OThkN2RiNzJmZDhhMzNlMWQ4Y2I4ZmMKGQiGiN6Yndi1imMQ_uKtwgYYsws4CEAKSAQQAxoGbWFsaXZhIiBlODkxY2ZkZTRhZWQwOTJlMjhkNTE2NmRhZTQ4NWI5MA",
  " csrf_session_id":"386f0ada851dc52ab81b4be010b8f8b3",
  " d_ticket":"9b30a730996fedb3ca6e5f070b355655dd8e7",
  " odin_tt":"a57fd8c08521d2717222af1081264c03d761bbf23f085b4b7834132ea3886b5eb1fb6ac3c546337de658569877399ba6f8af4a3ca6c18b2a34198dfec13e16d635e46626b390f5130a3bf7be02ad4fa1",
  " tt_csrf_token":"ApHbLRXc-YquV5tKYwbzstkhL18MNd6-BSto",
  " tta_attr_id_mirror":"0.1752023745.7524884686012137488",
  " tt_chain_token":"tDM9sPQF8fQQxHdaqNkYkg==",
  " delay_guest_mode_vid":"8",
  " perf_feed_cache":"^{^%^22expireTimestamp^%^22:1756432800000^%^2C^%^22itemIds^%^22:^[^%^227513348536755408133^%^22^%^2C^%^227537727079295569157^%^22^%^2C^%^227505111207997705478^%^22^]^}",
  " tiktok_webapp_theme":"light",
  " tiktok_webapp_theme_source":"light",
  " ttwid":"1^%^7CN4j_7_y2FHxuWVOVOEji2AmG1co5VTam6v8-HfpBABw^%^7C1755145757^%^7Cbece9c8a6f4e0983a83767b04963235f92babfaa866ddbb6627cd204b6bb41e8",
  " passport_fe_beating_status":"true",
  " msToken":"XTpaqs9CHuUlzXPrVUr9pyvbnl32qAUs79dGXJFlU7EkJ6uAoreE2kNFHI9-T-ah6xtDPVMb1tIzZvQE1B2vPzehqPQevf4rDj8ZjwIeYE6dLPcyPGM5W2NZ-PYx-_2tAcX8F_HWzVfvzTovAS23XsKe",
  " store-country-sign":"MEIEDGjUVm_y4Gu0fnigQQQgpTqKtuPGklgazTNLWGl2a8dGDNIRUhI7bPQNS49X3xIEEERnqXMEA0FdTUuuUcSsVHE",
  " msToken":"PdoZIN2YfRHU1QfkYdL3X4N3iJT9Md4RVkFzv848VvdvyBsJBsZuf-dRTgJ4MqG5uuDoeFOW-pCFBYBqB-jsOFRO5NFwGwYJs9ThZymSC6bkm1XZ_HXbeztdSITJIh5yQnSjYEQMAyJRrwjgHY0xEo7B^"
}
respuestas=[]

for url in urls:
    response = requests.get(url, headers=headers, cookies=cookies)
    respuestas.append(response.text)

df = pd.DataFrame(respuestas, columns=['Response'])
df.to_csv('responses2.csv', index=False, encoding='utf-8')