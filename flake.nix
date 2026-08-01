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
      # pdfjam: the pdf-screen cover/back trim step (declared here
      # 2026-07-31 — it had been leaking in from the host profile).
      texlive = pkgs.texliveSmall.withPackages (ps: with ps; [ pdfjam ]);

      # The book's faces (TeX Gyre Heros + Pagella), DECLARED — the
      # third leak of the undeclared-host-dep class (google-chrome,
      # pdfjam, now fonts; found by the valueof.info deploy sandbox
      # 2026-08-01): texliveSmall ships no TeX Gyre font files, and
      # desktop builds silently picked them up from the system X11
      # font set. FONTCONFIG_FILE below pins fontconfig to exactly
      # this set, so the shell cannot lean on host fonts and a
      # headless server builds identically. (The apt path was already
      # honest: AGENTS.md lists fonts-texgyre.)
      fontsConf = pkgs.makeFontsConf { fontDirectories = [ pkgs.gyre-fonts ]; };
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        FONTCONFIG_FILE = fontsConf;
        packages = with pkgs; [
          gyre-fonts
          # Writing / build (white-buffalo pipeline: Makefile + assemble-style scripts)
          git
          git-lfs # transcripts/raw/ JSONL archive (attribution process)
          gnumake
          pandoc
          texlive
          vale

          # Coding footprint (heftier than WB by design: wargaming models,
          # ledger tooling, fetch scripts). ruff + jq also serve the
          # user-level PostToolUse lint hooks.
          (python3.withPackages (ps: with ps; [ numpy pytest pillow ]))
          ruff
          uv
          jq

          # PDF work: reading, QA renders, page surgery
          poppler-utils # pdftotext, pdftoppm, pdfinfo, pdfseparate, pdfunite
          qpdf

          # Map plates: SVG -> vector PDF via rsvg-convert
          # (Chrome-free assembly, 2026-07-31 — replaces the
          # undeclared host google-chrome that scripts/svg2pdf.py
          # leaned on; librsvg sets plate labels through the same
          # fontconfig route xelatex uses for Pagella)
          librsvg

          # Reference shelf: doctrine pubs arrive as scanned PDFs
          ocrmypdf # OCR layer for scanned docs (pulls tesseract + ghostscript)

          # eBook edition (make epub; planning/ebook-brief.md):
          # epubcheck is the validation gate the target's artifacts
          # are held to; libxml2's xmllint for poking at the
          # unzipped XHTML. (calibre — viewer/converter — weighed
          # and left out: ~1 GB closure for a manual-use tool; add
          # it here if eBook work becomes recurring.)
          epubcheck
          libxml2

          # Fetching and unpacking reference documents
          curl
          unzip # also handy for epub inspection

          # GitHub operations (repo creation/administration — the
          # holdings private-remote task, PR work if any). SSH push
          # auth already lives at the user level; gh covers the API
          # side.
          gh
        ];

        shellHook = ''
          echo "The Mission (1986) environment ready."
        '';
      };
    };
}
