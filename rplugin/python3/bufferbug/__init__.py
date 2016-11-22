import neovim


@neovim.plugin
@neovim.encoding(True)
class IPythonPlugin(object):

    def __init__(self, vim):
        self.vim = vim
        self.buf = None

    def create_outbuf(self):
        vim = self.vim
        if self.buf is not None:
            return
        w0 = vim.current.window
        vim.command(":new")
        buf = vim.current.buffer
        buf.options["swapfile"] = False
        buf.options["buftype"] = "nofile"
        buf.name = "[jupyter]"
        vim.current.window = w0
        self.buf = buf

    @neovim.function("BufferBugInit")
    def init(self, args):
        self.create_outbuf()

    @neovim.function("BufferBug")
    def bug(self, args):
        self.buf.append(['multiple', 'lines', 'with', 'some', 'text'])
