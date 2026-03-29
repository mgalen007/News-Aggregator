import puppeteer from 'puppeteer'
import fs from 'fs/promises'

(async() => {
    // Pages to scrape
    const sections = ['politiki', 'ubukungu', 'imikino', 'ikoranabuhanga', 'amakuru']
    try {
        // Launch Chromium browser
        const browser = await puppeteer.launch({
            headless: false
        })

        // Open new tab
        const page = await browser.newPage()
        await page.setViewport(null)

        // Extract the headlines
        for (let section of sections) {
            const filename = `../api/reports/${section}.json`

            await page.goto(`https://igihe.com/${section}`, {
                waitUntil: 'networkidle2'
            })

            await page.waitForSelector('.homenews-title > a')
            const headlines = await page.$$eval(
                '.homenews-title > a',
                elts => elts.map(elt => ({
                    text: elt.textContent,
                    link: elt.href
                }))
            )
            await fs.appendFile(
                filename,
                JSON.stringify({
                    date: new Date().toString(),
                    page: section,
                    headlines
                }) + '\n'
            )
            console.log(`Wrote report to ${filename}`)
        }
        await browser.close()
    } catch(err) {
        console.error(err)
    }
})()