# Deploying LLM on Mobile

This guide provides a step-by-step process for deploying a Large Language Model (LLM) on mobile devices using Termux and Debian.

## Prerequisites

- Android device (Android 8.0 or higher)
- At least 4GB of RAM (8GB recommended)
- Sufficient storage space (minimum 8GB free)

## Step 1: Download Termux APK

Download the relevant version of the Termux APK for your phone. This guide uses the version compatible with Android 8.0.

- [Download Termux 0.101 APK](#)

## Step 2: Install Termux APK

1. Enable installation from unknown sources:
   - Navigate to **Settings > Apps & Notifications > Security**
   - Toggle on **Unknown sources**
2. Download the APK file from a trusted website
3. Install the APK by tapping the downloaded file

## Step 3: Grant Storage Permissions

1. Open Termux and grant storage permissions:
   ```bash
   termux-setup-storage
   ```
2. Allow access when prompted
3. Verify storage access to:
   - `storage/downloads`: Access to Downloads folder
   - `storage/shared`: Shared storage (main storage)
   - `storage/dcim`: Camera images
   - `storage/music` and `storage/pictures`: Media folders

## Step 4: Update Termux and Install Required Packages

1. Update Termux packages:
   ```bash
   pkg update && pkg upgrade
   ```
2. Install `proot-distro`:
   ```bash
   pkg install proot-distro
   ```

## Step 5: Install Debian

1. Install Debian:
   ```bash
   proot-distro install debian
   ```
   Shortcut: Use `pd install debian`

2. Launch Debian:
   ```bash
   proot-distro login debian
   ```

## Step 6: Configure Debian

1. Update Debian packages:
   ```bash
   apt update && apt upgrade
   ```
2. Install essential packages:
   ```bash
   apt install wget
   ```
3. Exit Debian (optional):
   ```bash
   exit
   ```

## Step 7: Install Ollama

1. Download the install script:
   ```bash
   wget https://ollama.ai/install.sh
   ```
2. Run the script:
   ```bash
   sh ./install.sh
   ```

## Step 8: Start Ollama Service

Start the Ollama service in the background:
```bash
ollama serve &
```

## Step 9: Run a Model

Execute a model using:
```bash
ollama run <model_name>
```
Example: `ollama run llama2`

## RAM Optimization (Optional)

To optimize RAM usage on Android devices:

### 1. Limit Background Processes
- Go to **Settings > Developer Options**
- Set **Background Process Limit** to 1-2 processes

### 2. Disable/Limit Animations
- Adjust the following settings in Developer Options:
  - **Window Animation Scale**: `0.5x` or `Off`
  - **Transition Animation Scale**: `0.5x` or `Off`
  - **Animator Duration Scale**: `0.5x` or `Off`

### 3. Don't Keep Activities
- Enable **Don't Keep Activities** under **Developer Options**

### 4. Force GPU Rendering
- Enable GPU rendering in Developer Options for better memory management

### 5. Limit System Apps
- Disable unnecessary system apps under **Settings > Apps**

## Important Notes

- Ensure your device meets the minimum requirements before installation
- Monitor device temperature during model execution
- Use trusted sources for APK downloads and scripts
- Back up important data before proceeding
- Some models may require additional configuration

## Troubleshooting

If you encounter issues:
1. Verify all permissions are correctly granted
2. Ensure sufficient storage space is available
3. Check system resources usage
4. Restart Termux if services become unresponsive

## Security Considerations

- Only download APKs from official sources
- Keep Termux and Debian packages updated
- Use secure network connections when downloading models
- Monitor system resource usage
