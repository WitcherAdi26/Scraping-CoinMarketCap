Scraping Assignment : CoinMarketCap
(Ignis Tech Solutions)

Name : Aditya Vijay Kalambkar
Email : kalambkar26@gmail.com


**Libraries used :**
django
djangorestframeworks
selenium
decouple
webdriver_manager
redis
pandas
openpyxl



# Lets look at the output given by the api


1) **Job_Id : 919d938b-6341-46f6-995c-667d6e0c7ad1**

**Requests made :** 
i) 
![POST REQ](<POST Start-Scraping Request-Response.png>)

ii) 
![GET REQ (PENDING)](<GET Scraping-Status PENDING.png>)

iii) 
![GET REQ (SUCCESS)](<GET Scraping-Status SUCCESS.png>)


**Responses received for :**

iii)
{
    "job_id": "919d938b-6341-46f6-995c-667d6e0c7ad1",
    "status": "SUCCESS",
    "task": [
        {
            "coin": "ethereum",
            "output": {
                "price": 3691.77,
                "price_change": -2.76,
                "market_cap": "443558257798",
                "market_cap_rank": 2,
                "volume": "16037501852",
                "volume_rank": 3,
                "volume_change": 3.63,
                "circulating_supply": "120147950",
                "total_supply": "120147950",
                "diluted_market_cap": "443558257798",
                "contracts": [
                    {
                        "name": "BNB Smart Chain (BEP20):",
                        "address": "0x2170...f933f8 "
                    }
                ],
                "official_links": [
                    {
                        "name": "Whitepaper",
                        "link": "https://github.com/ethereum/wiki/wiki/White-Paper"
                    },
                    {
                        "name": "GitHub",
                        "link": "https://github.com/ethereum/go-ethereum"
                    }
                ],
                "socials": [
                    {
                        "name": "𝕏\nTwitter",
                        "url": "https://twitter.com/ethereum"
                    },
                    {
                        "name": "Reddit",
                        "url": "https://reddit.com/r/ethereum"
                    },
                    {
                        "name": "Chat",
                        "url": "https://gitter.im/orgs/ethereum/rooms"
                    }
                ]
            }
        },
        {
            "coin": "DUKO",
            "output": {
                "price": 0.004783,
                "price_change": -13.1,
                "market_cap": "46220417",
                "market_cap_rank": 660,
                "volume": "12166421",
                "volume_rank": 392,
                "volume_change": 26.32,
                "circulating_supply": "9663955990",
                "total_supply": "9999609598",
                "diluted_market_cap": "47825769",
                "contracts": [
                    {
                        "name": "Solana:",
                        "address": "HLptm5...2G7rf9 "
                    }
                ],
                "official_links": [
                    {
                        "name": "Website",
                        "link": "https://dukocoin.com/"
                    }
                ],
                "socials": [
                    {
                        "name": "𝕏\nTwitter",
                        "url": "https://twitter.com/dukocoin"
                    },
                    {
                        "name": "Telegram",
                        "url": "https://t.me/+jlScZmFrQ8g2MDg8"
                    }
                ]
            }
        },
        {
            "coin": "usd-coin",
            "output": {
                "price": 1.0,
                "price_change": 0.01,
                "market_cap": "32189572236",
                "market_cap_rank": 6,
                "volume": "5709062693",
                "volume_rank": 5,
                "volume_change": 17.81,
                "circulating_supply": "32186712711",
                "total_supply": "32186712711",
                "diluted_market_cap": "32189572236",
                "contracts": [
                    {
                        "name": "Ethereum:",
                        "address": "0xa0b8...06eb48 "
                    }
                ],
                "official_links": [
                    {
                        "name": "Website",
                        "link": "https://www.centre.io/usdc"
                    },
                    {
                        "name": "Whitepaper",
                        "link": "https://f.hubspotusercontent30.net/hubfs/9304636/PDF/centre-whitepaper.pdf"
                    },
                    {
                        "name": "GitHub",
                        "link": "https://github.com/centrehq/centre-tokens"
                    }
                ],
                "socials": [
                    {
                        "name": "𝕏\nTwitter",
                        "url": "https://twitter.com/circle"
                    }
                ]
            }
        },
        {
            "coin": "XRP",
            "output": {
                "price": 0.494,
                "price_change": -5.74,
                "market_cap": "27420881963",
                "market_cap_rank": 7,
                "volume": "2138027760",
                "volume_rank": 8,
                "volume_change": 7.8,
                "circulating_supply": "55506158411",
                "total_supply": "99987553871",
                "diluted_market_cap": "49407386089",
                "contracts": [
                    {
                        "name": "BNB Smart Chain (BEP20):",
                        "address": "0x1d2f...c60dbe "
                    }
                ],
                "official_links": [
                    {
                        "name": "Website",
                        "link": "https://xrpl.org/"
                    },
                    {
                        "name": "Whitepaper",
                        "link": "https://ripple.com/files/ripple_consensus_whitepaper.pdf"
                    },
                    {
                        "name": "GitHub",
                        "link": "https://github.com/ripple/rippled"
                    }
                ],
                "socials": [
                    {
                        "name": "𝕏\nTwitter",
                        "url": "https://twitter.com/Ripple"
                    },
                    {
                        "name": "Reddit",
                        "url": "https://reddit.com/r/ripple"
                    }
                ]
            }
        }
    ]
}


**Django admin :**
![Django Admin](<Django admin.png>)


**Celery Console :**
![Celery Console](<Celery Console.png>)


**Django Console :**
![Django Console](<Djang Console.png>)






2) **Job_Id : 25336f36-34fd-4bc7-bdd7-28a1f538ca30**

**Requests Made :**

i) [08/Jun/2024 21:16:31] "POST /api/taskmanager/start_scraping HTTP/1.1" 202 50
Json-Body: 
{
    "payload":[
        "bitcoin",
        "solana",
        "dogecoin",
        "avalanche",
        "filecoin"
    ]
}


ii) [08/Jun/2024 21:16:45] "GET /api/taskmanager/scraping_status/25336f36-34fd-4bc7-bdd7-28a1f538ca30 HTTP/1.1" 200 71


iii) [08/Jun/2024 21:17:17] "GET /api/taskmanager/scraping_status/25336f36-34fd-4bc7-bdd7-28a1f538ca30 HTTP/1.1" 200 3454



**Responses Received :**

i)
{
    "job_id": "25336f36-34fd-4bc7-bdd7-28a1f538ca30"
}


ii)
{
    "job_id": "25336f36-34fd-4bc7-bdd7-28a1f538ca30",
    "status": "PENDING"
}


iii)
{
    "job_id": "25336f36-34fd-4bc7-bdd7-28a1f538ca30",
    "status": "SUCCESS",
    "task": [
        {
            "coin": "bitcoin",
            "output": {
                "price": 69438.01,
                "price_change": -1.99,
                "market_cap": "1368588231187",
                "market_cap_rank": 1,
                "volume": "26196254751",
                "volume_rank": 2,
                "volume_change": 1.91,
                "circulating_supply": "19709496",
                "total_supply": "19709496",
                "diluted_market_cap": "1458786163858",
                "contracts": [],
                "official_links": [
                    {
                        "name": "Reddit",
                        "link": "https://reddit.com/r/bitcoin"
                    }
                ],
                "socials": []
            }
        },
        {
            "coin": "solana",
            "output": {
                "price": 160.16,
                "price_change": -5.47,
                "market_cap": "73763819061",
                "market_cap_rank": 5,
                "volume": "3225623352",
                "volume_rank": 6,
                "volume_change": 4.37,
                "circulating_supply": "460571214",
                "total_supply": "577712451",
                "diluted_market_cap": "92650810097",
                "contracts": [],
                "official_links": [
                    {
                        "name": "𝕏\nTwitter",
                        "link": "https://twitter.com/solana"
                    },
                    {
                        "name": "Reddit",
                        "link": "https://reddit.com/r/solana"
                    },
                    {
                        "name": "Telegram",
                        "link": "https://t.me/solana"
                    },
                    {
                        "name": "Chat",
                        "link": "https://solana.com/discord"
                    }
                ],
                "socials": []
            }
        },
        {
            "coin": "dogecoin",
            "output": {
                "price": 0.1466,
                "price_change": -8.35,
                "market_cap": "21201337579",
                "market_cap_rank": 8,
                "volume": "1698725766",
                "volume_rank": 10,
                "volume_change": 8.0,
                "circulating_supply": "144624976384",
                "total_supply": "144624976384",
                "diluted_market_cap": "21235014214",
                "contracts": [
                    {
                        "name": "BNB Smart Chain (BEP20):",
                        "address": "0xba2a...744c43 "
                    }
                ],
                "official_links": [
                    {
                        "name": "Website",
                        "link": "http://dogecoin.com/"
                    },
                    {
                        "name": "Whitepaper",
                        "link": "https://github.com/dogecoin/dogecoin/blob/master/README.md"
                    },
                    {
                        "name": "GitHub",
                        "link": "https://github.com/dogecoin/dogecoin"
                    }
                ],
                "socials": [
                    {
                        "name": "𝕏\nTwitter",
                        "url": "https://twitter.com/dogecoin"
                    },
                    {
                        "name": "Reddit",
                        "url": "https://reddit.com/r/dogecoin"
                    },
                    {
                        "name": "Chat",
                        "url": "http://webchat.freenode.net/?nick=Shibe..&channels=%23dogecoin&prompt=1"
                    }
                ]
            }
        },
        {
            "coin": "avalanche",
            "output": {
                "price": 32.51,
                "price_change": -10.06,
                "market_cap": "12783171429",
                "market_cap_rank": 12,
                "volume": "600615972",
                "volume_rank": 20,
                "volume_change": 4.69,
                "circulating_supply": "393254529",
                "total_supply": "442600899",
                "diluted_market_cap": "23298444415",
                "contracts": [
                    {
                        "name": "Avalanche X-Chain:",
                        "address": "FvwEAh...CgxN5Z "
                    }
                ],
                "official_links": [
                    {
                        "name": "Whitepaper",
                        "link": "https://www.avalabs.org/whitepapers"
                    },
                    {
                        "name": "GitHub",
                        "link": "https://github.com/ava-labs/avalanchego"
                    }
                ],
                "socials": [
                    {
                        "name": "𝕏\nTwitter",
                        "url": "https://twitter.com/Avax"
                    },
                    {
                        "name": "Reddit",
                        "url": "https://reddit.com/r/Avax"
                    },
                    {
                        "name": "Facebook",
                        "url": "https://www.facebook.com/avalancheavax"
                    },
                    {
                        "name": "Telegram",
                        "url": "https://t.me/avalancheavax"
                    },
                    {
                        "name": "Chat",
                        "url": "https://chat.avax.network/"
                    }
                ]
            }
        },
        {
            "coin": "filecoin",
            "output": {
                "price": 6.17,
                "price_change": -7.07,
                "market_cap": "3466647686",
                "market_cap_rank": 29,
                "volume": "676972808",
                "volume_rank": 18,
                "volume_change": 19.54,
                "circulating_supply": "561737040",
                "total_supply": "1960252833",
                "diluted_market_cap": "12090581519",
                "contracts": [
                    {
                        "name": "BNB Smart Chain (BEP20):",
                        "address": "0x0d8c...9ae153 "
                    }
                ],
                "official_links": [
                    {
                        "name": "Website",
                        "link": "https://filecoin.io/"
                    },
                    {
                        "name": "Whitepaper",
                        "link": "https://docs.filecoin.io/"
                    },
                    {
                        "name": "GitHub",
                        "link": "https://github.com/filecoin-project/"
                    }
                ],
                "socials": [
                    {
                        "name": "𝕏\nTwitter",
                        "url": "https://twitter.com/Filecoin"
                    }
                ]
            }
        }
    ]
}
