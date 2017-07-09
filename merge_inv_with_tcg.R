# @title: merge_inv_with_tcg.py
# @author: Phuc Duong <phuchduong>
# @start_date: July 8th, 2017
# @email: phuchduong@hotmail.com
# description: merge inventory sheet with tcgplayer price list

setwd("D:/repos/mtg_toolkit")
inv = read.csv("inventory.csv", stringsAsFactors = FALSE)
tcg = read.csv("tcgplayer/tcg_prices.csv", stringsAsFactors = FALSE)

# filters
q.has_nf = !is.na(inv$nf_qty)   # non-foil quantity not null
q.has_f = !is.na(inv$f_qty)     # foil quantity not null
q.has_blk = !is.na(inv$is_bulk) # bulk is not null

# query only rows that are not null for quantities and bulk column
# only get back the first 4 columns
inv2 <- inv[
    q.has_nf | q.has_f | q.has_blk,
    c("card_name", "nf_qty", "f_qty", "is_bulk")
]

tcg$key <- tolower(tcg$card_name)

q.exists_in_tcg <- inv2$card_name %in% tcg$key
inv2[!q.exists_in_tcg,]

write.csv(x=inv2, file = "inventory.csv", row.names = FALSE)