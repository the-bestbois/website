# The Bestbois Frontend

This application is powered by [Svelte](https://svelte.dev/docs/kit).

## Developing

Install all dependencies:

```sh
pnpm install
```

Once finished, start a development server:

```sh
pnpm run dev
```

You can also start the server and immediately open the app in a new browser tab:

```sh
pnpm run dev -- --open
```

## Linting & Formatting

Before commiting changes, lint the code with ESLint...

```sh
pnpm run lint
```

...then fix any issues and format the code with Prettier:

```sh
pnpm run format
```

## Building

To create a production version of this app:

```sh
npm run build
```

You can preview the production build with `npm run preview`.

## Translating

This project uses [Paraglide](https://paraglidejs.com/sveltekit), which relies
on the `project.inlang/` directory for its configuration. By default,
the language files are stored as JSON in `messages/` that can be edited
directly.

If you use VSCode, a recommended extension to install is
[Sherlock](https://open-vsx.org/vscode/item?itemName=inlang.vs-code-extension)
that adds an intuitive editor with useful easy configuration, translation
and some useful inline commands.

> [!IMPORTANT]
> Paraglide turns translation files into JavaScript code that provides a simple
> syntax for accessing strings as function calls, as shown below.
>
> ```js
> m.hello();
> // Alternatively:
> m['nested.key']();
> ```
>
> As a result, editing the plugin's config or updating keys may behave
> unpredictably. So, if you're going to edit the translations, it is advised
> to first stop the server (even if it's in development mode), do edits,
> and then restart it.
>
> You can explore the generated code under `src/lib/paraglide/messages/`.
