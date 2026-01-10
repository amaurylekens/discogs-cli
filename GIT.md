## naming convention

### branch naming

**Branch** → *why does this work exist?* (intent)

```
<type>/<short-description>--<TICKET>
```

- `feat` → new feature
- `fix` → bug fix
- `hotfix` → urgent production fix
- `chore` → maintenance / setup / dependencies
- `refactor` → code refactoring (no feature or fix)
- `docs` → documentation changes
- `experiment` → adding or updating tests
- `perf` → performance improvements
- `ci` → CI/CD, pipelines, workflows

### commit messages

**Commit** → *what changed?* (action)

```
<type>(<scope>): <description> [<Ticket URL>]
```

- `feat` → new functionality
- `fix` → bug fix
- `refactor` → code change without behavior change
- `perf` → performance improvement
- `test` → add / update tests
- `docs` → documentation only
- `style` → formatting (no logic change)
- `chore` → tooling, deps, config, scripts
- `ci` → CI/CD changes
- `build` → build system changes
- `revert` → revert a previous commit

Commit scopes are project-specific and must map to the codebase’s architectural components, not to a universal or shared list.