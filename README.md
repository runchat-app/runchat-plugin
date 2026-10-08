# Runchat plugins

Plugins that connect AI assistants to [Runchat](https://runchat.com), a node-based canvas for design workflows.

- [`runchat/`](runchat/) is the Claude plugin: the Runchat connector plus a skill. Install it in Claude Code with:

  ```bash
  claude plugin marketplace add runchat-app/runchat-plugin
  claude plugin install runchat@runchat
  ```

- [`chatgpt/`](chatgpt/) is the source for the ChatGPT plugin package. Build the ZIP with `python scripts/build_chatgpt_zip.py`, which also bundles the skill from `runchat/skills/`.

Both point at the same remote MCP server, `https://runchat.com/api/mcp`. See [runchat/README.md](runchat/README.md) for what the plugin does and what data it sends.
