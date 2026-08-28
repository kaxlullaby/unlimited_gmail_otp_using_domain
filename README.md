# unlimited_gmail_using_domain
sesuai judul aja mas


Kalo pakai cloudflare pasti relate, kalo enggak ya paling settingnya sama2 aja

1. beli domain yg murah/pakai yg udah ada
2. pastikan domain lu udh proxied di CF
3. masuk CF, pilih domain, pilih "email > email routing"
4. klik get started
5. nnti klo diminta tambahin record MX & TXT iyain aja
6. di email routing klik destination addresses
7. klik add destination
8. masukin email utama/yg mau di jdiin tmpt verif, ntar CF ngasih verif
9. masih di email routing, klik routing rules
10. cari bagian Catch-all-adress, trus edit
11. pilih send to email utama/yg mau dijadiin tmpt verif lu tadi
12. save


Tips Pro buat Scaling Massal
Filter Gmail:
             Bikin filter di Gmail: from:@domainlo.com -> Skip Inbox, Apply Label "OTP Bot".
             Biar inbox utama gak penuh sampah.
IMAP Automation:
                Kalau mau full auto, konekin Gmail ke script via IMAP.
                Pake library imaplib atau gmail-api buat baca OTP otomatis.
Subdomain Trick:
                Kalau Cloudflare limit catch-all, lo bisa bikin subdomain: bot1.domainlo.com, bot2.domainlo.com.
                Setup Email Routing terpisah buat tiap subdomain (tapi biasanya catch-all udah cukup buat ribuan email).
Warm-up Domain:
               Jangan langsung kirim 1000 request dalam 1 menit.
               Spread out registrasi: 50 akun/jam dulu, naikin pelan-pelan biar domain gak kena blacklist spam.
Reply-to Address:
               Beberapa platform (kayak Gmail sendiri) butuh verifikasi reply-to.
               Cloudflare Email Routing support Custom Reply-To. Setup di dashboard kalau diperlukan.
