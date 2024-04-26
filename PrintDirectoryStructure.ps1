# PowerShell script to print a formatted directory structure to a text file
function Print-DirectoryStructure {
    param (
        [string]$path = ".",
        [int]$indentLevel = 0,
        [string]$outputFile = "DirectoryStructure.txt"
    )

    # Excluded directories
    $excludedDirectories = @("venv", "__pycache__")

    # Write the formatted path to the file
    "$('  ' * $indentLevel)|-- $($path | Split-Path -Leaf)" | Out-File -Append -LiteralPath $outputFile

    try {
        # Get immediate subdirectories in the directory excluding specified ones
        $subdirectories = Get-ChildItem -LiteralPath $path | Where-Object { $_.PSIsContainer -and $_.Name -notin $excludedDirectories }

        # Write items with appropriate indentation and formatting to the file
        foreach ($subdir in $subdirectories) {
            # Recursively call the function for subdirectories
            Print-DirectoryStructure -path $subdir.FullName -indentLevel ($indentLevel + 1) -outputFile $outputFile
        }

        # Get files in the directory
        $files = Get-ChildItem -LiteralPath $path | Where-Object { -not $_.PSIsContainer -and $_.Name -notin $excludedDirectories }

        # Write files with appropriate indentation to the file
        foreach ($file in $files) {
            "$('  ' * ($indentLevel + 1))|-- $($file.Name)" | Out-File -Append -LiteralPath $outputFile
        }
    }
    catch {
        "$('  ' * ($indentLevel + 1))|-- Error: $_" | Out-File -Append -LiteralPath $outputFile
    }
}

# Example usage with output to a file
Print-DirectoryStructure -path "C:\Users\Goerner\Desktop\pedestrian_network" -outputFile "DirectoryStructureOutput.txt"