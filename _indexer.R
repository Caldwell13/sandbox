indexer <- function(p) {
     data <- read.xlsx(p, sheetIndex = 1, startRow = 1, endRow = 5, header = FALSE)
     date <- data[1,2]
     notebook <- data[2,2]
     title <- data[3,2]
     keyword <- as.character(data[4,2])
     reference <- data[5,2]
     if (length(keyword) == 0) {" "}
     else if(is.null(keyword) | is.na(keyword)) {
          q <- data[1,8]
          paste(q, "\t", "\t", "\t", "\t", "Keywords:", notebook)
     }
     else {
          paste(notebook, "\t", "Date:", date, "\t", "Title:", title, "\t", "Keywords:", keyword, "\t", "Reference:", reference)
     }
}

filelister <- function() {
     library(xlsx)
     library(xlsxjars)
     li <- list.files(pattern = glob2rx("MAC-*-*.xlsx"), recursive = TRUE, include.dirs = TRUE)
     lines <- vector()
     for (i in 1:length(li)){
          lines[i] <- indexer(li[i])
          i <- i+1
     }
     sort(lines, decreasing = TRUE)
     file.create("_index.tsv", overwrite = TRUE)
     print("file created")
     write(lines, file = "_index.tsv")
     file.remove("TRUE")
}