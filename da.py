import asyncio
from pyppeteer import launch
from pyppeteer.errors import TimeoutError


def conv_to_int(rp_str):
    strConv = str(rp_str)
    res_str = strConv.replace('Rp', '').replace(' ', '').replace('.', '')
    try:
        result = int(res_str)
        return result
    except ValueError:
        return None


async def scrape_panel_harga(url):
    try:
        browser = await launch()
        page = await browser.newPage()
        await page.goto(url)

        await page.waitForSelector('div[style="display:flex;flex-direction:column;justify-content:space-between;align-items:flex-start;height:100%;"]')

        data_list = []

        elements = await page.querySelectorAll('div[style="display:flex;flex-direction:column;justify-content:space-between;align-items:flex-start;height:100%;"]')
        for element in elements:
            title = await element.querySelectorEval('span.price-item-title', 'el => el.textContent')
            price = await element.querySelectorEval('span.price-item-price', 'el => el.textContent')
            unit = await element.querySelectorEval('span.price-item-per', 'el => el.textContent')

            data_list.append((title.strip(), price.strip(), unit.strip()))

        await browser.close()

        for data in data_list:
            print(data[0])
            # komoditi = ImageKomoditas.objects.get(
            #     nama=str(data[0]))
            # print(komoditi)
            # InfoHarga.objects.create(komoditas=komoditi, price=conv_to_int(
            #     data[1]), per_price=str(data[2]))
            # info = InfoHarga(
            #     komoditas=komoditas,
            #     price=conv_to_int(data[1]),
            #     per_price=str(data[2])
            # )
            # info.save()

        print("helloddd")
        return data_list
    except TimeoutError:
        print("Timeout error: Halaman tidak dimuat sepenuhnya dalam waktu yang ditentukan.")
    except Exception as e:
        print(f"Error: {str(e)}")


def do_scraping_info_harga():
    try:
        urls = "https://panelharga.badanpangan.go.id/"
        # scrape_panel_data_request_bsoup(url=url)
        asyncio.get_event_loop().run_until_complete(scrape_panel_harga(url=urls))
        # scrape_panel_data(url=url)
        print("hello worldsssss")
        return "Scraping data successfully."
    except Exception as e:
        msg = "Failed to scraping data - %s" % str(e)
        # logger.error(msg)
        return msg

do_scraping_info_harga()