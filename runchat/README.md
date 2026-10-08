# Runchat

![Runchat](assets/logo.png)

Runchat is a node-based canvas for design workflows used by architects, designers and computational designers. This plugin connects Claude to your Runchat account so Claude can build, edit and run workflows on your canvas, publish finished workflows as reusable tools and hosted pages, and script the design software you already have open (Rhino, Grasshopper and Blender) through the Runchat desktop plugins.

## What's included

- **Runchat connector**: the remote MCP server at `https://runchat.com/api/mcp`. You sign in with your Runchat account through OAuth the first time Claude uses it.
- **`runchat` skill**: short guidance on how Claude should use the connector, including confirming before it spends credits, publishes, or changes a document open in a desktop app.

## What you can do

- Find, create, copy and organize runchat workflows, and add prompt, media, code, input and note nodes.
- Run workflows and get back their outputs. Runs that call AI models spend credits from your Runchat account.
- Publish a workflow as a tool, and create or update hosted pages (blog posts, websites and apps) with private, team or public visibility.
- Read and script an open Rhino, Grasshopper or Blender session, and capture its viewport, when the Runchat plugin is running in that app and signed in to the same account.
- Edit screen recordings in the ClipChat desktop app.
- Search the web, fetch pages and search the Runchat docs.

## Requirements

- A Runchat account. Sign up at [runchat.com](https://runchat.com).
- Credits on that account for runs that call AI models.
- For desktop tools, the Runchat plugin for Rhino, Grasshopper or Blender, or the ClipChat app, installed from [docs.runchat.com](https://docs.runchat.com).

## Data and network use

This plugin contains no code that runs on your machine. It adds the Runchat connector and a skill. Requests go only to `https://runchat.com/api/mcp`, authenticated with your Runchat OAuth token. Runchat then calls the AI model providers your workflows use, and relays desktop commands to your own signed-in desktop apps. What Runchat stores and shares is described in the [privacy policy](https://runchat.com/privacy). Terms of use are at [runchat.com/terms](https://runchat.com/terms).

## Support

Contact us at [runchat.com/contact](https://runchat.com/contact) or read the docs at [docs.runchat.com](https://docs.runchat.com).
