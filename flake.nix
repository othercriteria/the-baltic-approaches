{
  description = "The Mission (1986) - writing and document environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };

      # xetex + fontsrecommended (TeX Gyre Pagella) covers the
      # white-buffalo-style book build; extra collections are cheap to
      # add here later if the interior design asks for them.
      texlive = pkgs.texliveSmall;
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        packages = with pkgs; [
          # Writing / build (white-buffalo pipeline: Makefile + assemble-style scripts)
          git
          git-lfs # transcripts/raw/ JSONL archive (attribution process)
          gnumake
          pandoc
          texlive
          python3
          vale

          # PDF work: reading, QA renders, page surgery
          poppler-utils # pdftotext, pdftoppm, pdfinfo, pdfseparate, pdfunite
          qpdf

          # Reference shelf: doctrine pubs arrive as scanned PDFs
          ocrmypdf # OCR layer for scanned docs (pulls tesseract + ghostscript)

          # Fetching and unpacking reference documents
          curl
          unzip # also handy for epub inspection
        ];

        shellHook = ''
          echo "The Mission (1986) environment ready."
        '';
      };
    };
}
