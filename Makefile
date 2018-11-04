.PHONY: clean

DOCNAME = thesis

thesis.pdf: $(TEXSOURCES) $(DOCNAME).bib
	@rm -f $(DOCNAME).{aux,toc,lof,lot}
	(rm -f pdflatex $(DOCNAME) && bibtex $(DOCNAME) && pdflatex $(DOCNAME) && pdflatex $(DOCNAME)) || rm -f $(DOCNAME).pdf
	@rm -f $(DOCNAME).{aux,toc,lof,lot}

clean:
	@rm -f $(DOCNAME).{pdf,log,aux}
	@rm -f *.bbl *.blg *.lof *.cut
	@rm -f *.lot *.out *.toc
