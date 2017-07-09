# @title: check_for_spell_mistakes.R
# @author: Phuc Duong <phuchduong>
# @start_date: July 8th, 2017
# @email: phuchduong@hotmail.com
# description:  cross references inventory card name with tcgplayer card
#               names to find spelling mistakes.

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

# Retest again for spelling mistakes
inv = read.csv("inventory.csv", stringsAsFactors = FALSE)
tcg = read.csv("tcgplayer/tcg_prices.csv", stringsAsFactors = FALSE)

tcg$key <- tolower(tcg$card_name)
q.exists_in_tcg <- inv$card_name %in% tcg$key
inv[!q.exists_in_tcg,]
