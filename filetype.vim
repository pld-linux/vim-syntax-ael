" put this file to $HOME/.vim
if exists("have_load_filetypes")
      finish
endif
augroup filetypedetect
      au! BufRead,BufNewFile *.ael	setfiletype ael
augroup END
