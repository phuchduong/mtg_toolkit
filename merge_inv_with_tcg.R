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

# if the two rows do not match then that means there were duplications
# in the inventory sheet. go and remove them.
nrow(tcg2) == nrow(tcg.single)
#write.csv(tcg.single, file = "tcg_single.csv", row.names = FALSE)
#write.csv(tcg2, file = "tcg_merged.csv", row.names = FALSE)

# merge the two tcg sheets back together
tcg.reprint$nf_qty <- NA
tcg.reprint$f_qty <- NA
tcg.reprint$is_bulk <- NA
tcg3 <- rbind(tcg2, tcg.reprint, stringsAsFactors=FALSE)

# finds cards that have been reprinted, from inventory
inv.reprinted <- inv[!inv$card_name %in% tcg.single$key,]

# format the reprinted carsd to have same columns and unknown set
inv.reprinted$mana_cost <- NA
inv.reprinted$set_name <- "unknown set"
inv.reprinted$rarity <- NA
inv.reprinted$price_h <- NA
inv.reprinted$price_m <- NA
inv.reprinted$price_l <- NA
inv.reprinted$scrape_date <- NA
inv.reprinted$reprints <- NA
tcg3$key <- NULL
tcg4 <- rbind(tcg3, inv.reprinted, stringsAsFactors=FALSE)

write.csv(x=tcg4, file="inventory 2017-07-09.csv", row.names = FALSE)
