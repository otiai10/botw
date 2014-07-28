package botw

import "go/ast"
import "go/token"

func GetAllControllerNames(pkg *ast.Package) (names []string) {
	for _, f := range pkg.Files {
		for _, decl := range f.Decls {
			if genDecl, ok := decl.(*ast.GenDecl); ok {
				if genDecl.Tok != token.TYPE {
					// This is not `type`
					continue
				}
				spec := genDecl.Specs[0].(*ast.TypeSpec)
				names = append(names, spec.Name.String())
			}
		}
	}
	return
}
