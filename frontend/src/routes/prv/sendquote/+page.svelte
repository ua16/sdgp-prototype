<script>
    import ProviderNav from "$lib/components/provider/ProviderNav.svelte";
    import ProviderContainer from "$lib/components/provider/ProviderContainer.svelte";
    import ProviderSendQuote from "$lib/components/provider/ProviderSendQuote.svelte";

    import { onMount } from "svelte";

    let isSignedIn = false;
    onMount(() => {
        isSignedIn = localStorage.getItem("signedin") === "true";
    });
</script>

<div>
    {#if isSignedIn === false}
        <p>404 Not Found</p>

    {:else}
        <ProviderContainer>
            <ProviderNav />
            <ProviderSendQuote />
        </ProviderContainer>
    {/if}
</div>
