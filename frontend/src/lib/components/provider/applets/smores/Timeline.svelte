<script lang="ts">
    let { quotedata } = $props();

    const dateFormatter = new Intl.DateTimeFormat("en-US", {
        year: "numeric",
        month: "short", // or 'long', 'numeric', '2-digit'
        day: "numeric",
        hour: "numeric",
        minute: "2-digit",
        hour12: true, // for AM/PM
    });

function formatDate(dateString : string): string {
    const date = new Date(dateString.replace(' ', 'T'));

    return dateFormatter.format(date);
}

</script>

<div
    class="flex flex-col gap-3 w-full bg-stone-100 border-stone-300 border-2 p-3 text-stone-700 rounded-2xl"
>
    <div class="font-bold text-xl">Timeline</div>

    <div class="flex flex-col">
        <div class="stone-300">Quote Sent Date: {formatDate(quotedata.creationDate)}</div>
        <div class="stone-300">Target Delivery: {formatDate(quotedata.deliveryDate)}</div>
    </div>

    <hr class="border-stone-300" />

    <div class="rounded-2xl bg-stone-200 p-2 flex flex-col">
        <div class="text-sm text-stone-800">Quote Deadline</div>
        <div class="text-lg text-stone-800">{formatDate(quotedata.expiryDate)}</div>
    </div>
</div>
