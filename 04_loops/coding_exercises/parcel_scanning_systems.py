# This function will be tested automatically.
# Do not change the function name or parameters.
def scan_parcels(parcel_codes: list[str]) -> list[str]:
    # Write your code below this line
    log=[]
    for barcode in parcel_codes:
        if barcode=="DAMAGED":
            log.append("Skipped damaged parcel")
            continue
        if barcode=="STOP":
            log.append("Critical error: Stopping scan")
            break
        log.append(f"Scanned parcel: {barcode}")
    else:
        log.append("All parcels scanned successfully" )
    return log
    pass