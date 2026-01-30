# Starting JupyterLab in Codespaces

JupyterLab is pre-installed in your codespace environment. To start it:

1. Open a terminal in your VSCode codespace (Terminal → New Terminal)
2. Run the following command:
   ```bash
   jupyter lab --allow-root
   ```
3. The terminal will display a URL with an authentication token. Look for a line like:
   ```
   http://127.0.0.1:8888/lab?token=...
   ```
   Copy the token info *after* the "...token=". We'll need it in the next step.

4. In VS Code, you should see a notification asking if you want to open the forwarded port, or you can:
   - Click on the "Ports" tab in the bottom panel
   - Find port 8888 in the list
   - Click the "Open in Browser" icon (globe icon) next to port 8888
5. JupyterLab will open in a new browser tab. Enter the token (from step 3) into the authentication field when prompted.

**Note:** Port 8888 is automatically forwarded in Codespaces, so you don't need to manually configure port forwarding.

Alternatively you can set up the software environment locally on your own computer, see the [setup instructions](README.md). 

Or start a JupyterLab session on UVA's HPC system as [described here](hpc.md#login-via-web-browser).

