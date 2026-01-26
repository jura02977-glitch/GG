            try:
                import requests
                import json
                import base64
                
                # Encode image to base64
                # Go back to start of file to read it again
                f.seek(0)
                image_bytes = f.read()
                base64_image = base64.b64encode(image_bytes).decode('utf-8')
                
                # Prepare API call
                api_key = "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" # Hardcoded per request
                
                response = requests.post(
                  url="https://openrouter.ai/api/v1/chat/completions",
                  headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                    # "HTTP-Referer": "https://genieschool.up.railway.app", 
                    # "X-Title": "GenieSchool", 
                  },
                  data=json.dumps({
                    "model": "allenai/molmo-2-8b:free",
                    "messages": [
                      {
                        "role": "user",
                        "content": [
                          {
                            "type": "text",
                            "text": "Extract the National Identification Number (NIN) from this Identity Card image. It is usually a long sequence of digits (9 to 20 digits). Return ONLY the number digits, no other text."
                          },
                          {
                            "type": "image_url",
                            "image_url": {
                              "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                          }
                        ]
                      }
                    ]
                  }),
                  timeout=30 
                )
                
                if response.status_code == 200:
                    ai_response = response.json()
                    content = ai_response['choices'][0]['message']['content']
                    print(f"AI OCR Raw Response: {content}")
                    
                    # Clean and extract digits
                    import re
                    # Remove non-digit characters to be safe
                    possible_nin = re.sub(r'\D', '', content)
                    
                    # Basic validation (e.g. at least 8 digits)
                    if len(possible_nin) >= 8:
                        student.nin = possible_nin
                        print(f"NIN Detected and saved: {possible_nin}")
                    else:
                        print(f"AI returned invalid NIN content: {content}")
                else:
                    print(f"OpenRouter API Error: {response.status_code} - {response.text}")

            except Exception as ocr_error:
                print(f"OCR Error: {ocr_error}")
            # ---------------------------                   if not f:
