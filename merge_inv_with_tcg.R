# @title: merge_inv_with_tcg.py
# @author: Phuc Duong <phuchduong>
# @start_date: July 8th, 2017
# @email: phuchduong@hotmail.com
# description: merge inventory sheet with tcgplayer price list

setwd("D:/repos/mtg_toolkit")
inv = read.csv("inventory.csv", stringsAsFactors = FALSE)
tcg = read.csv("tcgplayer/tcg_prices.csv", stringsAsFactors = FALSE)

tcg$key <- tolower(tcg$card_name)
tcg.single <- tcg[tcg$reprints==1,]
tcg.reprint <- tcg[tcg$reprints!=1,]

tcg2 = merge(x = tcg.single, y = inv, by.x = "key", by.y = "card_name", all.x = TRUE, all.y = FALSE)

write.csv(tcg.single, file = "tcg_single.csv", row.names = FALSE)
write.csv(tcg2, file = "tcg_merged.csv", row.names = FALSE)
