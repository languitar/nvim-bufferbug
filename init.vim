scriptencoding utf8
if !has('nvim')
    set encoding utf8
end

" bundle settings
set nocompatible
filetype off

call plug#begin('~/.local/share/nvim/bundle/')

Plug 'languitar/nvim-bufferbug'

call plug#end()

filetype plugin indent on
