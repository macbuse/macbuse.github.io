-- https://wikimatze.de/vimtex-the-perfect-tool-for-working-with-tex-and-vim/

-- Install packer
local install_path = vim.fn.stdpath 'data' .. '/site/pack/packer/start/packer.nvim'

if vim.fn.empty(vim.fn.glob(install_path)) > 0 then
  vim.fn.execute('!git clone https://github.com/wbthomason/packer.nvim ' .. install_path)
end

vim.api.nvim_exec(
  [[
  augroup Packer
    autocmd!
   autocmd BufWritePost init.lua PackerCompile
  augroup end
]],
  false
)

local use = require('packer').use
require('packer').startup(function()
	-- use 'navarasu/onedark.nvim'
	use 'wbthomason/packer.nvim' -- Package manager
	use 'folke/tokyonight.nvim'
	use "folke/twilight.nvim"
	use "folke/zen-mode.nvim"
	use 'tpope/vim-fugitive' -- Git commands in nvim
	-- use 'tpope/vim-rhubarb' -- Fugitive-companion to interact with github
	use 'tpope/vim-commentary' -- "gc" to comment visual regions/lines
	use 'tpope/vim-surround' -- 
	use 'ludovicchabant/vim-gutentags' -- Automatic tags management
	-- UI to select things (files, grep results, open buffers...)
	-- use 'nvim-lua/popup.nvim'
	use { 'nvim-telescope/telescope.nvim', requires = { 'nvim-lua/plenary.nvim','nvim-lua/popup.nvim' } }
	use 'itchyny/lightline.vim' -- Fancier statusline
	-- Add indentation guides even on blank lines
	use 'lukas-reineke/indent-blankline.nvim'
	-- Add git related info in the signs columns and popups
	use { 'lewis6991/gitsigns.nvim', requires = { 'nvim-lua/plenary.nvim' } }
	-- translate to french using google translate
	use 'uga-rosa/translate.nvim'
	use {
	  "ahkohd/buffer-sticks.nvim",
	  config = function()
	    require("buffer-sticks").setup()
	  end
	}
	-- Highlight, edit, and navigate code using a fast incremental parsing library
	use 'nvim-treesitter/nvim-treesitter'
	-- Additional textobjects for treesitter
	use 'nvim-treesitter/nvim-treesitter-textobjects'
	-- nvim-cmp'
	--
	--
	-- use 'sirver/ultisnips'
	-- use "quangnguyen30192/cmp-nvim-ultisnips"

	use {
		"hrsh7th/nvim-cmp",
		requires = {
			{ "neovim/nvim-lspconfig" },
			{ "hrsh7th/cmp-nvim-lsp" },
			{ "hrsh7th/cmp-nvim-lua" },
			{ "hrsh7th/cmp-vsnip" },
			{ "hrsh7th/vim-vsnip" },
			{ "hrsh7th/cmp-path" },
			{ "hrsh7th/cmp-buffer" },
			{ "hrsh7th/cmp-cmdline" },
			{ "amarakon/nvim-cmp-lua-latex-symbols" },
			-- vscode like pic on suggestion
			--
			--{ "quangnguyen30192/cmp-nvim-ultisnips",
			--	config = function()
			--		-- optional call to setup (see customization section)
			--		require("cmp_nvim_ultisnips").setup {}
			--	end,
			--	--
			--	-- sources = { { name = "ultisnips" }}
			--}

		}
	}

-- use 'prabirshrestha/vim-lsp'
-- use 'mattn/vim-lsp-settings'
	--#region


use 'neovim/nvim-lspconfig' -- Collection of configurations for built-in LSP client

  use 'saadparwaiz1/cmp_luasnip'
  use 'L3MON4D3/LuaSnip' -- Snippets plugin


use { "iurimateus/luasnip-latex-snippets.nvim",
  requires = { "L3MON4D3/LuaSnip", "lervag/vimtex" },
  -- using treesitter.
  -- requires = { "L3MON4D3/LuaSnip", "nvim-treesitter/nvim-treesitter" },
  config = function()
    require'luasnip-latex-snippets'.setup()
  -- using treesitter.
    -- require'luasnip-latex-snippets'.setup({ use_treesitter = true })
    require("luasnip").config.setup { enable_autosnippets = true }

  end,
  -- treesitter is required for markdown
  -- ft = { "tex", "markdown" },
  ft = { "tex"}
}

vim.g.tex_flavor = 'latex'
---
  -- Diverse
--  use 'junegunn/goyo.vim'
  -- use 'junegunn/limelight.vim'
  use 'reedes/vim-pencil'
  -- use 'mhinz/vim-startify'
use {
  "startup-nvim/startup.nvim",
  requires = {"nvim-telescope/telescope.nvim", "nvim-lua/plenary.nvim", "nvim-telescope/telescope-file-browser.nvim"},
  config = function()
    require"startup".setup()
  end
}

use 'nvim-telescope/telescope-media-files.nvim'
	--
use {
 'iamcco/markdown-preview.nvim',
 ft = 'markdown',
 run = 'cd app && yarn install'
}

-- use {
--     "Exafunction/codeium.nvim",
--     requires = {
--         "nvim-lua/plenary.nvim",
--         "hrsh7th/nvim-cmp",
--     },
--     config = function()
--         require("codeium").setup({
--         })
--     end
-- }

use {'github/copilot.vim', branch = 'release' }
-- use {'benlubas/molten-nvim', version = "^1.0.0"}
-- use { 'dccsillag/magma-nvim', run = ':UpdateRemotePlugins' }
use{ "kiyoon/jupynium.nvim",
    build = "pip3 install --user ."}

-- use {
--   "zbirenbaum/copilot.lua",
--   cmd = "Copilot",
--   event = "InsertEnter",
--   config = function()
--     require("copilot").setup({})
--   end,
-- }

-- use {
--   "zbirenbaum/copilot-cmp",
--   after = { "copilot.lua" },
--   config = function ()
--     require("copilot_cmp").setup()
--   end
-- }

use {'lervag/vimtex',
    config = function()
      vim.cmd([[
        let g:vimtex_view_method = 'zathura'
        let g:vimtex_view_general_viewer = 'zathura'
        let g:vimtex_view_enabled=1
	let g:vimtex_quickfix_mode=0
	set conceallevel=1
	let g:tex_conceal='abdmg'
      ]])
    end
  }
end)

--Incremental live completion (note: this is now a default on master)
vim.o.inccommand = 'nosplit'

--Set highlight on search
vim.o.hlsearch = false

--Make line numbers default
--<leader>nn to toggle
vim.wo.number = false

--Do not save when switching buffers (note: this is now a default on master)
vim.o.hidden = true

--Enable mouse mode
-- vim.o.mouse = 'c' --'a'
-- fuck off mouse
vim.cmd [[
set mouse = 
]]

--Enable break indent
vim.o.breakindent = true

--Save undo history
vim.opt.undofile = true

--Case insensitive searching UNLESS /C or capital in search
vim.o.ignorecase = true
vim.o.smartcase = true

--Decrease update time
vim.o.updatetime = 250
vim.wo.signcolumn = 'yes'

--Set colorscheme (order is important here)
vim.o.termguicolors = false
vim.g.background = 'dark'
vim.g.t_Co = 256

-- should match with tty theme
 vim.cmd [[colorscheme tokyonight-storm]]

--Set statusbar
vim.g.lightline = {
  colorscheme = 'tokyonight',
  active = { left = { { 'mode', 'paste' }, { 'gitbranch', 'readonly', 'filename', 'modified' } } },
  component_function = { gitbranch = 'fugitive#head' },
}

--Remap space as leader key
vim.api.nvim_set_keymap('', '<Space>', '<Nop>', { noremap = true, silent = true })
vim.g.mapleader = ' '
vim.g.maplocalleader = ' '

--Remap for dealing with word wrap
vim.api.nvim_set_keymap('n', 'k', "v:count == 0 ? 'gk' : 'k'", { noremap = true, expr = true, silent = true })
vim.api.nvim_set_keymap('n', 'j', "v:count == 0 ? 'gj' : 'j'", { noremap = true, expr = true, silent = true })

-- Highlight on yank
vim.api.nvim_exec(
  [[
  augroup YankHighlight
    autocmd!
    autocmd TextYankPost * silent! lua vim.highlight.on_yank()
  augroup end
]],
  false
)


--Map blankline
vim.g.indent_blankline_char = '┊'
vim.g.indent_blankline_filetype_exclude = { 'help', 'packer' }
vim.g.indent_blankline_buftype_exclude = { 'terminal', 'nofile' }
vim.g.indent_blankline_char_highlight = 'LineNr'
vim.g.indent_blankline_show_trailing_blankline_indent = false


---- Telescope
----
--require('telescope').setup {
--  defaults = {
--    mappings = {
--      i = {
--        ['<C-u>'] = false,
--        ['<C-d>'] = false,
--      },
--    },
--  },
--}

require("telescope").setup({
	defaults = {
		layout_config = {
			horizontal = {
				preview_cutoff = 0,
			},
		},
	},
	extensions = {
		media_files = {
			-- filetypes whitelist
			-- defaults to {"png", "jpg", "mp4", "webm", "pdf"}
			filetypes = { "png", "webp", "jpg", "jpeg" },
			-- find command (defaults to `fd`)
			find_cmd = "rg"
		}
	}

})

require('telescope').load_extension('media_files')

--Add leader shortcuts
vim.api.nvim_set_keymap('n', '<leader><space>', [[<cmd>lua require('telescope.builtin').buffers()<CR>]], { noremap = true, silent = true })
vim.api.nvim_set_keymap('n', '<leader>sf', [[<cmd>lua require('telescope.builtin').find_files({previewer = true})<CR>]], { noremap = true, silent = true })
vim.api.nvim_set_keymap('n', '<leader>sb', [[<cmd>lua require('telescope.builtin').current_buffer_fuzzy_find()<CR>]], { noremap = true, silent = true })
vim.api.nvim_set_keymap('n', '<leader>sh', [[<cmd>lua require('telescope.builtin').help_tags()<CR>]], { noremap = true, silent = true })
vim.api.nvim_set_keymap('n', '<leader>st', [[<cmd>lua require('telescope.builtin').tags()<CR>]], { noremap = true, silent = true })
vim.api.nvim_set_keymap('n', '<leader>sd', [[<cmd>lua require('telescope.builtin').grep_string()<CR>]], { noremap = true, silent = true })
vim.api.nvim_set_keymap('n', '<leader>sp', [[<cmd>lua require('telescope.builtin').live_grep()<CR>]], { noremap = true, silent = true })
vim.api.nvim_set_keymap('n', '<leader>so', [[<cmd>lua require('telescope.builtin').tags{ only_current_buffer = true }<CR>]], { noremap = true, silent = true })
vim.api.nvim_set_keymap('n', '<leader>?', [[<cmd>lua require('telescope.builtin').oldfiles()<CR>]], { noremap = true, silent = true })

-- Treesitter configuration
-- Parsers must be installed manually via :TSInstall
require('nvim-treesitter.configs').setup {
  highlight = {
    enable = true, -- false will disable the whole extension
  },
  incremental_selection = {
    enable = true,
    keymaps = {
      init_selection = 'gnn',
      node_incremental = 'grn',
      scope_incremental = 'grc',
      node_decremental = 'grm',
    },
  },
  indent = {
    enable = true,
  },
  textobjects = {
    select = {
      enable = true,
      lookahead = true, -- Automatically jump forward to textobj, similar to targets.vim
      keymaps = {
        -- You can use the capture groups defined in textobjects.scm
        ['af'] = '@function.outer',
        ['if'] = '@function.inner',
        ['ac'] = '@class.outer',
        ['ic'] = '@class.inner',
      },
    },
    move = {
      enable = true,
      set_jumps = true, -- whether to set jumps in the jumplist
      goto_next_start = {
        [']m'] = '@function.outer',
        [']]'] = '@class.outer',
      },
      goto_next_end = {
        [']M'] = '@function.outer',
        [']['] = '@class.outer',
      },
      goto_previous_start = {
        ['[m'] = '@function.outer',
        ['[['] = '@class.outer',
      },
      goto_previous_end = {
        ['[M'] = '@function.outer',
        ['[]'] = '@class.outer',
      },
    },
  },
}

-- LSP settings
local nvim_lsp = require 'lspconfig'
local on_attach = function(_, bufnr)
  vim.api.nvim_buf_set_option(bufnr, 'omnifunc', 'v:lua.vim.lsp.omnifunc')

  local opts = { noremap = true, silent = true }
  vim.api.nvim_buf_set_keymap(bufnr, 'n', 'gD', '<Cmd>lua vim.lsp.buf.declaration()<CR>', opts)
  vim.api.nvim_buf_set_keymap(bufnr, 'n', 'gd', '<Cmd>lua vim.lsp.buf.definition()<CR>', opts)
  vim.api.nvim_buf_set_keymap(bufnr, 'n', 'K', '<Cmd>lua vim.lsp.buf.hover()<CR>', opts)
  vim.api.nvim_buf_set_keymap(bufnr, 'n', 'gi', '<cmd>lua vim.lsp.buf.implementation()<CR>', opts)
  vim.api.nvim_buf_set_keymap(bufnr, 'n', '<C-k>', '<cmd>lua vim.lsp.buf.signature_help()<CR>', opts)
  vim.api.nvim_buf_set_keymap(bufnr, 'n', '<leader>wa', '<cmd>lua vim.lsp.buf.add_workspace_folder()<CR>', opts)
  vim.api.nvim_buf_set_keymap(bufnr, 'n', '<leader>wr', '<cmd>lua vim.lsp.buf.remove_workspace_folder()<CR>', opts)
  vim.api.nvim_buf_set_keymap(bufnr, 'n', '<leader>wl', '<cmd>lua print(vim.inspect(vim.lsp.buf.list_workspace_folders()))<CR>', opts)
  vim.api.nvim_buf_set_keymap(bufnr, 'n', '<leader>D', '<cmd>lua vim.lsp.buf.type_definition()<CR>', opts)
  vim.api.nvim_buf_set_keymap(bufnr, 'n', '<leader>rn', '<cmd>lua vim.lsp.buf.rename()<CR>', opts)
  vim.api.nvim_buf_set_keymap(bufnr, 'n', 'gr', '<cmd>lua vim.lsp.buf.references()<CR>', opts)
  vim.api.nvim_buf_set_keymap(bufnr, 'n', '<leader>ca', '<cmd>lua vim.lsp.buf.code_action()<CR>', opts)
  -- vim.api.nvim_buf_set_keymap(bufnr, 'v', '<leader>ca', '<cmd>lua vim.lsp.buf.range_code_action()<CR>', opts)
  vim.api.nvim_buf_set_keymap(bufnr, 'n', '<leader>e', '<cmd>lua vim.lsp.diagnostic.show_line_diagnostics()<CR>', opts)
  vim.api.nvim_buf_set_keymap(bufnr, 'n', '[d', '<cmd>lua vim.lsp.diagnostic.goto_prev()<CR>', opts)
  vim.api.nvim_buf_set_keymap(bufnr, 'n', ']d', '<cmd>lua vim.lsp.diagnostic.goto_next()<CR>', opts)
  vim.api.nvim_buf_set_keymap(bufnr, 'n', '<leader>q', '<cmd>lua vim.lsp.diagnostic.set_loclist()<CR>', opts)
  vim.api.nvim_buf_set_keymap(bufnr, 'n', '<leader>so', [[<cmd>lua require('telescope.builtin').lsp_document_symbols()<CR>]], opts)
  vim.cmd [[ command! Format execute 'lua vim.lsp.buf.formatting()' ]]
end

-- nvim-cmp supports additional completion capabilities
local capabilities = vim.lsp.protocol.make_client_capabilities()
capabilities = require('cmp_nvim_lsp').default_capabilities()

-- Enable the following language servers
local servers = { 'clangd', 'rust_analyzer', 'pyright', 'texlab'}
-- texlab has to be installed using cargo 
-- so needs Rust to be installed first

for _, lsp in ipairs(servers) do
  nvim_lsp[lsp].setup {
    on_attach = on_attach,
    capabilities = capabilities,
  }
end

-- apparently this will never work
-- require('lspconfig').texlab.setup {
-- 	on_attach = on_attach,
-- 	capabilities = capabilities,
-- 	settings = {
-- 		ft = { 'tex', 'md' } } }

-- Example custom server
local sumneko_root_path = vim.fn.getenv 'HOME' .. '/.local/bin/sumneko'

local sumneko_binary = sumneko_root_path .. '/bin/lua-language-server'
-- Make runtime files discoverable to the server
local runtime_path = vim.split(package.path, ';')
table.insert(runtime_path, 'lua/?.lua')
table.insert(runtime_path, 'lua/?/init.lua')

require('lspconfig').sumneko_lua.setup {
  cmd = { sumneko_binary, '-E', sumneko_root_path .. '/main.lua' },
  on_attach = on_attach,
  capabilities = capabilities,
  settings = {
    Lua = {
      runtime = {
        -- Tell the language server which version of Lua you're using (most likely LuaJIT in the case of Neovim)
        version = 'LuaJIT',
        -- Setup your lua path
        path = runtime_path,
      },
      diagnostics = {
        -- Get the language server to recognize the `vim` global
        globals = { 'vim' },
      },
      workspace = {
        -- Make the server aware of Neovim runtime files
        library = vim.api.nvim_get_runtime_file('', true),
      },
      -- Do not send telemetry data containing a randomized but unique identifier
      telemetry = {
        enable = false,
      },
    },
  },
}

-- require("lspconfig.health").check()

-- Set completeopt to have a better completion experience
vim.o.completeopt = 'menuone,noselect'

-- luasnip setup
local luasnip = require 'luasnip'

-- nvim-cmp setup
local cmp = require 'cmp'
cmp.setup {
  snippet = {
    expand = function(args)
      require('luasnip').lsp_expand(args.body)
    end,
  },
  mapping = {
    ['<C-p>'] = cmp.mapping.select_prev_item(),
    ['<C-n>'] = cmp.mapping.select_next_item(),
    ['<C-d>'] = cmp.mapping.scroll_docs(-4),
    ['<C-f>'] = cmp.mapping.scroll_docs(4),
    ['<C-Space>'] = cmp.mapping.complete(),
    ['<C-e>'] = cmp.mapping.close(),
    ['<CR>'] = cmp.mapping.confirm {
      behavior = cmp.ConfirmBehavior.Replace,
      select = true,
    },
    ['<Tab>'] = function(fallback)
      if vim.fn.pumvisible() == 1 then
        vim.fn.feedkeys(vim.api.nvim_replace_termcodes('<C-n>', true, true, true), 'n')
      elseif luasnip.expand_or_jumpable() then
        vim.fn.feedkeys(vim.api.nvim_replace_termcodes('<Plug>luasnip-expand-or-jump', true, true, true), '')
      else
        fallback()
      end
    end,
    ['<S-Tab>'] = function(fallback)
      if vim.fn.pumvisible() == 1 then
        vim.fn.feedkeys(vim.api.nvim_replace_termcodes('<C-p>', true, true, true), 'n')
      elseif luasnip.jumpable(-1) then
        vim.fn.feedkeys(vim.api.nvim_replace_termcodes('<Plug>luasnip-jump-prev', true, true, true), '')
      else
        fallback()
      end
    end,
  },

	sources = {
		{ name = 'nvim_lsp' },
		{ name = 'path' },
		{ name = 'buffer' },
		{ name = 'luasnip' },
		{ name = 'ultisnips' },
		-- this doesn't appear to work with TS latex
		{ name = "lua-latex-symbols", option = { cache = true } }
	},
}

vim.o.spell = true
-- https://stackoverflow.com/questions/25777205/how-to-make-z-look-like-ctrl-x-s-in-vim-spell-check#comment116976526_25777332

vim.cmd[[
nnoremap <leader>s :call search('\w\>', 'c')<CR>a<C-X><C-S>
inoremap <expr> <leader><leader> pumvisible() ? "\<C-y><Esc>" : "\<CR>"
]]

-- vim.api.nvim_set_keymap('n', '<leader>s', ":call search('\w\>', 'c')<CR>a<C-X><C-S>", { noremap = true, silent = true })


-- google search
--
vim.keymap.set("v", "<leader>g", function()

	vim.cmd('normal! "vy') -- Yank selected text into register v
	local selected_text = vim.fn.getreg('v') 
	vim.fn.setreg('v', '') 
	-- selected_text = vim.fn.escape(selected_text, "#?&+/ ")
	local search_url = "https://www.google.com/search?q=" .. selected_text

    -- Open in the default browser
    local open_cmd
    if vim.fn.has("mac") == 1 then
        open_cmd = "open '" .. search_url .. "'"
    elseif vim.fn.has("unix") == 1 then
        open_cmd = "xdg-open '" .. search_url .. "'"
    else
        print("Unsupported OS")
        return
    end
    -- Run the command 
vim.fn.system(open_cmd)
end, { desc = "Search selected text on Google", noremap = true, silent = true })

-- vim.api.nvim_set_keymap('v', '<leader>g', ':lua google_search()<CR>', { noremap = true, silent = true })

-- Chat interface
require("CopilotChat").setup {
  -- See Configuration section for options
}

vim.keymap.set("n", "<leader>cc",  ':CopilotChat ', { remap=false })
vim.keymap.set("x", "<leader>cc",  ':CopilotChatVisual ', { remap=false })
vim.keymap.set("n", "<leader>ccb",  ':CopilotChatBuffer ', { remap=false })
vim.keymap.set("x", "<leader>ccx",  ':CopilotChatInPlace<CR>', { remap=false })

-- https://stackoverflow.com/questions/4368690/how-to-increase-the-vertical-split-window-size-in-vim
vim.cmd [[
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

nmap <M-Right> :vertical resize +1<CR>
nmap <M-Left> :vertical resize -1<CR>
nmap <M-Down> :resize +1<CR>
nmap <M-Up> :resize -1<CR>
]]

-- Y yank until the end of line  (note: this is now a default on master)
vim.api.nvim_set_keymap('n', 'Y', 'y$', { noremap = true })

vim.api.nvim_set_keymap("n", "U", "<C-r>",{expr = false, noremap = true})
vim.api.nvim_set_keymap("n", "<C-v>", '"+p',{expr = false, noremap = true})

vim.api.nvim_set_keymap("n", "<leader>FF", 'gqip',{expr = false, noremap = true})

vim.o.textwidth = 68
vim.g.netrw_browse_split = 2
vim.g.netrw_winsize = 25

-- Map <Leader>nn to toggle line numbers
vim.api.nvim_set_keymap('n', '<Leader>nn', ':lua vim.wo.number = not vim.wo.number<CR>', { noremap = true, silent = true })
-- Map <Leader>bb to switch to the next buffer
-- vim.api.nvim_set_keymap('n', '<Leader>bb', ':bn<CR>', { noremap = true, silent = true })
-- delete till the end of a file
vim.api.nvim_set_keymap('n', '<Leader>de', ':.,$ d<CR>', { noremap = true, silent = true })
--run the current file it should have a shebang
vim.api.nvim_set_keymap('n', '<leader>pp', ':w<CR>:! ./%<CR>', { noremap = true, silent = true })
vim.api.nvim_set_keymap('n', '<leader>mm', ':MarkdownPreview<CR>', { noremap = true, silent = true })
vim.api.nvim_set_keymap('n', '<leader>ZZ', ':ZenMode<CR>', { noremap = true, silent = true })

-- keybindings for translate
vim.api.nvim_set_keymap('n', '<space>tw', 'viw:Translate FR<CR>', { noremap = true, silent = true })
-- Normal mode mapping
vim.api.nvim_set_keymap('n', 'vf', ':Translate FR<CR>', { noremap = true, silent = true })
vim.api.nvim_set_keymap('n', 'if', ':Translate FR -output=insert<CR>', { noremap = true, silent = true })

-- Visual mode mapping
vim.api.nvim_set_keymap('x', 'vf', ':Translate FR<CR>', { noremap = true, silent = true })
vim.api.nvim_set_keymap('x', 'if', ':Translate FR -output=insert<CR>', { noremap = true, silent = true })


vim.api.nvim_set_keymap('x', '<leader>yy', '"+y', { noremap = true, silent = true })
vim.api.nvim_set_keymap('n', '<leader>y', 'yc:<ctrl>R"<CR>', { noremap = true, silent = true })
vim.api.nvim_set_keymap('n', '<leader>aa', ':Startup display<CR>', { noremap = true, silent = true })
-- this replaces bn above
vim.api.nvim_set_keymap('n', '<leader>bb', ':lua BufferSticks.list()<CR>', { noremap = true, silent = true })

vim.g.clipboard = {
      name = 'OSC 52',
      copy = {
        ['+'] = require('vim.ui.clipboard.osc52').copy('+'),
        ['*'] = require('vim.ui.clipboard.osc52').copy('*'),
      },
      paste = {
        ['+'] = require('vim.ui.clipboard.osc52').paste('+'),
        ['*'] = require('vim.ui.clipboard.osc52').paste('*'),
      },
    }

vim.keymap.set("v", "<leader>ee", function()
    -- Get the start and end position of the visual selection
    vim.cmd('normal! "vy')  -- Yank selected text into register v
    local selected_text = vim.fn.getreg('v')  -- Get the yanked text
    vim.fn.setreg('v', '')  -- Clear the register to prevent stale data
 if #selected_text > 0 then
        print(selected_text)
end
    
    if selected_text and #selected_text > 0 then
        -- Wrap the selected text with **
        local wrapped_text = "**" .. selected_text .. "**"
        
        -- Replace the selection with the modified text
        vim.api.nvim_feedkeys(vim.api.nvim_replace_termcodes("gvc" .. wrapped_text .. "<Esc>", true, false, true), "x", false)
    end
end, { desc = "Surround selection with **", noremap = true, silent = true })

