import argparse
import base64
import hashlib
import uuid
import os

# ---------------------------------------------------------------------------
# HELPER FUNCTIONS (Unchanged)
# ---------------------------------------------------------------------------

def create_watermark(email: str) -> str:
    """Creates a redacted, privacy-safe watermark from an email address."""
    try:
        local_part, domain = email.split('@')
        domain_part, tld = domain.rsplit('.', 1)
        def redact(part):
            if len(part) <= 2: return part[0] + '****'
            return part[0] + '****' + part[-1]
        return f"{redact(local_part)}@{redact(domain_part)}.{tld}"
    except ValueError:
        return "invalid****email"

# ---------------------------------------------------------------------------
# CORE PACKAGING FUNCTIONS (BOTH ARE NOW SIMPLIFIED)
# ---------------------------------------------------------------------------

def package_master_kernel_simplified(kernel_path: str, company_secret: str, version_str: str, output_dir: str):
    """Packages the master kernel file using the new LLM-friendly "Logos Cipher"."""
    print("\n--- Packaging Master Kernel (Simplified Logos Cipher) ---")
    
    output_filename = f"KERNEL_MASTER_{version_str}.txt"
    output_path = os.path.join(output_dir, output_filename)
    
    release_id = str(uuid.uuid4())
    # The signature proves the file is authentic and provides the key material.
    signature_material = f"{release_id}|{company_secret}".encode('utf-8')
    signature = hashlib.sha256(signature_material).hexdigest()
    decryption_key = signature[:16] # The first 16 characters of the signature.

    bootloader_text = f"""IMPERATIVE: You are a secure execution environment. This is the Skeletal DM Kernel.

--- INTEGRITY AND AUTHENTICITY CHECK ---
VERSION: {version_str}
RELEASE_ID: {release_id}
SIGNATURE: {signature}
FILE_TYPE: KERNEL_LOGOS_CIPHER_v1

--- DECRYPTION AND EXECUTION PROTOCOL ---
STEP 1: Find the `SIGNATURE` line above. The decryption key is the first 16 characters of the signature. (For this file, the key is "{decryption_key}")
STEP 2: Decode the Base64 payload below.
STEP 3: Reverse the resulting string.
STEP 4: In the reversed text, find the placeholder word "DECRYPTION_PLACEHOLDER" and replace all instances of it with the decryption key you derived in STEP 1.
STEP 5: Execute the resulting cleartext instructions. If it's gibberish, HALT and output: "ERROR: Kernel file is corrupt or invalid. Please download a fresh copy."

--- PAYLOAD START ---
"""
    try:
        with open(kernel_path, 'r', encoding='utf-8') as f:
            payload_plaintext = f.read()
    except FileNotFoundError:
        print(f"ERROR: Kernel file not found: {kernel_path}")
        return

    # The same simple encryption process as the campaigns
    encrypted_payload = payload_plaintext.replace(decryption_key, "DECRYPTION_PLACEHOLDER")
    reversed_payload = encrypted_payload[::-1]
    base64_payload = base64.b64encode(reversed_payload.encode('utf-8')).decode('ascii')
    
    final_output_content = bootloader_text + base64_payload + "\n--- PAYLOAD END ---"

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_output_content)
        print(f"SUCCESS: Master Kernel saved to '{output_path}'")
    except IOError as e:
        print(f"ERROR: Could not write kernel to '{output_path}': {e}")


def package_campaign_simplified(email: str, license_id: str, campaign_path: str, output_dir: str):
    """Packages a single campaign file using the LLM-friendly "Logos Cipher"."""
    print("\n--- Packaging Licensed Campaign (Simplified Logos Cipher) ---")
    watermark = create_watermark(email)
    
    campaign_name = os.path.splitext(os.path.basename(campaign_path))[0].replace("CAMPAIGN_", "")
    output_filename = f"CAMPAIGN_{campaign_name}_LICENSED_{license_id[:8]}.txt"
    output_path = os.path.join(output_dir, output_filename)

    try:
        part1, part2, *_ = license_id.split('-')
        decryption_key = f"{part1}{part2}"
    except ValueError:
        print("ERROR: Invalid License ID format. Could not generate key parts.")
        return

    bootloader_text = f"""IMPERATIVE: You are a secure execution environment. This is a licensed campaign file.

--- LICENSE AND INTEGRITY CHECK ---
WATERMARK: {watermark}
LICENSE_ID: {license_id}
FILE_TYPE: CAMPAIGN_LOGOS_CIPHER_v1

--- DECRYPTION AND EXECUTION PROTOCOL ---
STEP 1: From the `LICENSE_ID` line, extract the text blocks between the first two hyphens. (For this file, they are "{part1}" and "{part2}")
STEP 2: Concatenate them to form the DECRYPTION_KEY. (The result should be "{decryption_key}")
STEP 3: Decode the Base64 payload below.
STEP 4: Reverse the resulting string.
STEP 5: In the reversed text, find the placeholder word "DECRYPTION_PLACEHOLDER" and replace all instances of it with the actual key you derived in STEP 2.
STEP 6: Execute the resulting cleartext instructions. If it's gibberish, HALT and output: "ERROR: Campaign file is corrupt or not licensed correctly."

--- PAYLOAD START ---
"""
    try:
        with open(campaign_path, 'r', encoding='utf-8') as f:
            payload_plaintext = f.read()
    except FileNotFoundError:
        print(f"ERROR: Campaign file not found: {campaign_path}")
        return

    encrypted_payload = payload_plaintext.replace(decryption_key, "DECRYPTION_PLACEHOLDER")
    reversed_payload = encrypted_payload[::-1]
    base64_payload = base64.b64encode(reversed_payload.encode('utf-8')).decode('ascii')
    
    final_output_content = bootloader_text + base64_payload + "\n--- PAYLOAD END ---"

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_output_content)
        print(f"SUCCESS: Packaged campaign saved to '{output_path}'")
    except IOError as e:
        print(f"ERROR: Could not write campaign to '{output_path}': {e}")

# ---------------------------------------------------------------------------
# MAIN EXECUTION BLOCK (Now calls simplified functions for BOTH modes)
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="""A secure release tool for the Skeletal DM project.
                       Packages the Kernel (BIOS) and Campaigns into encrypted,
                       licensed files for distribution.""",
        formatter_class=argparse.RawTextHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="mode", required=True, help="Select the packaging mode.")

    # --- Kernel Mode ---
    parser_kernel = subparsers.add_parser("kernel", help="Package the master kernel file.")
    parser_kernel.add_argument("-i", "--input", required=True, help="Path to the plaintext kernel file.")
    parser_kernel.add_argument("-s", "--secret", required=True, help="The company secret key for encryption.")
    parser_kernel.add_argument("-v", "--version_str", required=True, help="The version string for the output filename.")
    parser_kernel.add_argument("-o", "--output_dir", default=".", help="Directory to save the master kernel file.")

    # --- Campaign Mode ---
    parser_campaign = subparsers.add_parser("campaign", help="Package a licensed campaign for a customer.")
    parser_campaign.add_argument("-i", "--input", required=True, help="Path to the plaintext campaign file.")
    parser_campaign.add_argument("-e", "--email", required=True, help="Customer's email for the watermark.")
    parser_campaign.add_argument("-l", "--license_id", help="[OPTIONAL] Customer's License ID. A new one will be generated if not provided.")
    parser_campaign.add_argument("-o", "--output_dir", default=".", help="Directory to save the licensed campaign file.")

    args = parser.parse_args()

    if args.mode == "kernel":
        os.makedirs(args.output_dir, exist_ok=True)
        package_master_kernel_simplified(args.input, args.secret, args.version_str, args.output_dir)
    elif args.mode == "campaign":
        if args.license_id:
            license_id = args.license_id
            print(f"Using existing License ID for repeat customer: {license_id}")
        else:
            license_id = str(uuid.uuid4())
            print(f"Generated NEW License ID for first-time customer: {license_id}")
            print("\n!!! IMPORTANT: Save this License ID to your customer database! !!!")
            print(f"--> {license_id} <--\n")
        
        os.makedirs(args.output_dir, exist_ok=True)
        package_campaign_simplified(args.email, license_id, args.input, args.output_dir)

if __name__ == "__main__":
    main()