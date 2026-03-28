import puppeteer from 'puppeteer'

(async() => {
    try {
        // Launch Chromium browser
        const browser = await puppeteer.launch({
            headless: false
        })

        // Open new tab
        const page = await browser.newPage()

        // Navigate to igihe.com
        await page.goto('https://igihe.com/politiki', {
            waitUntil: 'networkidle2'
        })

        // Extract the headlines
        await page.waitForSelector('.homenews-title > a')
        const headlines = await page.$$eval(
            '.homenews-title > a',
            elts => elts.map(elt => ({
                text: elt.textContent,
                link: elt.href
            }))
        )
        console.log(headlines)
    } catch(err) {
        console.error(err)
    }
})()