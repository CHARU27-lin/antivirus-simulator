# Known malware database

MALWARE_SIGNATURES = {
    "44d88612fea8a8f36de82e1278abb02f": "EICAR-Test-Virus",
    "de967e95dbe61366acc5320800d49314": "Test,Virus",
}

def check_signature(file_hash):
    if file_hash in MALWARE_SIGNATURES:
        return True, MALWARE_SIGNATURES[file_hash]
    return False, None